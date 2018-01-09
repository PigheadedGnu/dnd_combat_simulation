from src.heuristics.heuristic_container import HeuristicContainer
from src.utils import *


class Combatant:
    def __init__(self, name, hp, ac, proficiency, saves, actions, heuristics=HeuristicContainer()):
        """
        :param hp: An integer of the creatures HP
        :param ac: An integer of the creatures AC
        :param saves: A dictionary of saves with each key being a 3-letter stat code
        :param actions: A list of action objects defined in actions.py
        :param heuristics: A list of strings that define heuristics for the creature
        """
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.ac = ac
        self.proficiency = proficiency
        self.saves = saves
        self.attacks = sorted([a for a in actions if a.action_type == "Attack"],
                              key=lambda x: x.calc_expected_damage(),
                              reverse=True)
        self.heals = sorted([a for a in actions if a.action_type == "Heal"],
                            key=lambda x: sum([num_dice * (max_roll/2.0+0.5)
                                               for num_dice, max_roll in x.dice.items()]),
                            reverse=True)
        self.num_actions_available = 1  # All creatures start with 1 available action
        self.heuristics = heuristics
        self.applied_effects = []

    @staticmethod
    def choose_action(action_set):
        for action in action_set:
            if not action.ready:
                action.try_recharge()
            if action.ready and action.num_available != 0:
                action.num_available -= 1
                action.ready = False
                return action

    def on_turn_start(self):
        if self.applied_effects is not None and len(self.applied_effects) > 0:
            for effect in self.applied_effects:
                effect.on_turn_start(self)

    def on_turn_end(self):
        if self.applied_effects is not None and len(self.applied_effects) > 0:
            for effect in self.applied_effects:
                still_active = effect.on_turn_end(self)
                if not still_active:
                    self.applied_effects.remove(effect)
        self.num_actions_available = 1

    def take_turn(self, allies, enemies, heuristic):
        self.on_turn_start()
        if self.hp < 0:
            return
        while self.num_actions_available > 0:
            self.num_actions_available -= 1
            self._try_heal(allies, heuristic)
            self._try_attack(enemies, heuristic)
        self.on_turn_end()

    def _try_attack(self, enemies, heuristic):
        attack = self.choose_action(self.attacks)
        for _ in range(attack.multi_attack):
            if enemies:
                target = self._choose_target(enemies,
                                             heuristic.attack_selection)
                if attack.aoe:
                    enemies = [e for e in enemies if e != target]
                attack.do_damage(self, target)
                attack.apply_effects(target)

    def _try_heal(self, allies, heuristic):
        heal_target = self._check_heal_need(allies, heuristic.heal_selection)
        available_heals = [h for h in self.heals if h.num_available > 0]
        if len(available_heals) > 0 and heal_target:
            heal = self.choose_action(self.heals)
            for _ in range(heal.num_targets):
                if heal_target is not None:
                    heal.do_heal(self, heal_target)
                    allies = [a for a in allies if a != heal_target]
                    heal_target = self._check_heal_need(
                        allies, heuristic.heal_selection)

    def _choose_target(self, enemies, heuristic):
        if self.heuristics.attack_selection:
            return self.heuristics.attack_selection.select(enemies)
        return heuristic.select(enemies)

    def _check_heal_need(self, allies, should_heal_heuristic):
        if self.heuristics.heal_selection:
            return self.heuristics.heal_selection.select(allies)
        return should_heal_heuristic.select(allies)

    def jsonify(self, write_to_file=True):
        """ Turn a creature object into JSON """
        combatant_info = {
            "name": self.name,
            "hp": self.max_hp,
            "ac": self.ac,
            "proficiency": self.proficiency,
            "saves": self.saves,
            "actions": [a.name for a in self.attacks] + [h.name for h in self.heals]
        }
        if write_to_file:
            write_json_to_file('combatants.json', combatant_info)
        return combatant_info
