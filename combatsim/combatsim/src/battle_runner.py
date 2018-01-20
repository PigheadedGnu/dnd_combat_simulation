import numpy as np
from src.heuristics import target_selection_heuristics
from src.managers.combatant_manager import CombatantManager
from src.simulator import Simulator

from combatsim.combatsim.src.heuristics.heuristic_container import \
    HeuristicContainer

heuristic_mapping = dict([(name, cls) for name, cls
                          in target_selection_heuristics.__dict__.items()
                          if isinstance(cls, type)])


class BattleRunner:
    def __init__(self):
        self.cm = CombatantManager()

    def run_simulator(self, team1_names, team2_names, num_sims,
                      attack_heuristic='Random', heal_heuristic='LowestHealth'):

        heuristics = HeuristicContainer(
            attack_selection=heuristic_mapping[attack_heuristic](),
            heal_selection=heuristic_mapping[heal_heuristic]())

        team1 = [self.cm.load_combatant(name) for name in team1_names]
        team2 = [self.cm.load_combatant(name) for name in team2_names]

        number_of_rounds = []
        number_of_player_deaths = []
        winning_teams = []
        for i in range(num_sims):
            sim = Simulator(team1, team2)
            num_rounds, num_player_deaths, winning_team = sim.run_battle(
                heuristics)
            number_of_player_deaths.append(num_player_deaths)
            winning_teams.append(winning_team)
            number_of_rounds.append(num_rounds)

        if num_sims > 1:
            print("Average number of rounds:", np.mean(number_of_rounds))
            print("Average number of player deaths",
                  np.mean(number_of_player_deaths))
            print("Number of times at least 1 player death:",
                  len([x for x in number_of_player_deaths if x > 0]))
            print("Percent of times players won:", 1 - np.mean(winning_teams))

            players_won = [number_of_rounds[i] for i in range(num_sims) if
                           winning_teams[i] == 0]
            monsters_won = [number_of_rounds[i] for i in range(num_sims) if
                            winning_teams[i] == 1]
            if players_won:
                print("Average number of rounds when player won:",
                      np.mean(players_won))
            if monsters_won:
                print("Average number of rounds when monsters won:",
                      np.mean(monsters_won))


if __name__ == "__main__":
    br = BattleRunner()
    br.run_simulator(["Marshall", "Johnny", "Max"],
                     ["Goblin"]*10,
                     200)
