from random import randint
from Creature import d20
from copy import deepcopy
from settings import VERBOSITY


class Simulator:
    def __init__(self, pcs, enemies):
        """
        :param pcs: A list of creatures that represent the PCs
        :param enemies: A list of creatures that represent the enemies in the battle
        """
        self.pcs = deepcopy(pcs)
        self.enemies = deepcopy(enemies)
        self.battle_order = None

    def calc_initiative(self):
        pc_initiative = [(pc, d20() + pc.saves['DEX']) for pc in self.pcs]
        enemies_initiative = [(enemy, d20() + enemy.saves['DEX']) for enemy in self.enemies]
        self.battle_order = [(t[0], 0 if t[0] in self.pcs else 1) for t in
                             sorted(pc_initiative + enemies_initiative, key=lambda x: x[1],
                                    reverse=True)]

    def run_round(self, heuristics):
        for creature, team in self.battle_order:
            if creature.hp <= 0:
                continue
            allies = [x[0] for x in self.battle_order if x[1] == team and x[0].hp > 0]
            enemies = [x[0] for x in self.battle_order if x[1] != team and x[0].hp > 0]
            if not enemies:
                break
            creature.act(allies, enemies, heuristics)

        dead_enemies = [c.name for c in self.enemies if c.hp <= 0]
        dead_pcs = [c.name for c in self.pcs if c.hp <= 0]

        self.battle_order = [c for c in self.battle_order if c[0].hp > 0]
        self.enemies = [c for c in self.enemies if c.hp > 0]
        self.pcs = [c for c in self.pcs if c.hp > 0]

        return dead_enemies, dead_pcs

    def run_battle(self, heuristics):
        num_player_deaths = 0
        round_num = 0
        self.calc_initiative()
        while self.enemies and self.pcs:
            if VERBOSITY > 1:
                print("---- Round {0} ----".format(round_num))
            enemies_dead, players_dead = self.run_round(heuristics)
            if players_dead:
                num_player_deaths += len(players_dead)

            if VERBOSITY > 0:
                if enemies_dead:
                    print("Round {0}".format(round_num), [e + " died" for e in enemies_dead])
                if players_dead:
                    print("Round {0}".format(round_num), [p + " died" for p in players_dead])

            round_num += 1
        winning_team = 0 if self.pcs else 1
        return round_num, num_player_deaths, winning_team

