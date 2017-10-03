from heuristics.HeuristicContainer import HeuristicContainer


class Creature:
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
                              key=lambda x: sum([num_dice * (max_roll/2.0+0.5)
                                                 for num_dice, max_roll in x.dice.items()]),
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

    def apply_effects(self):
        if self.applied_effects is not None and len(self.applied_effects) > 0:
            for effect in self.applied_effects:
                if effect.turns_left == 0:
                    self.applied_effects.remove(effect)
            [effect.affect(self) for effect in self.applied_effects]

    def act(self, allies, enemies, heuristic):
        heal_target = self._check_heal_need(allies, heuristic.heal_selection)

        self.apply_effects()
        if self.hp < 0:
            return
        while self.num_actions_available > 0:
            self.num_actions_available -= 1
            if len(self.heals) > 0 and heal_target:
                if heal_target and [h for h in self.heals if h.num_available > 0]:
                    heal = self.choose_action(self.heals)
                    heal.do_heal(self, heal_target)
            else:
                attack = self.choose_action(self.attacks)
                for _ in range(attack.multi_attack):
                    if enemies:
                        target = self._choose_target(enemies, heuristic.attack_selection)
                        attack.do_damage(self, target)
                        attack.apply_effects(target)

        self.num_actions_available = 1

    def _choose_target(self, enemies, heuristic):
        if self.heuristics.attack_selection:
            return self.heuristics.attack_selection.select(enemies)
        return heuristic.select(enemies)

    def _check_heal_need(self, allies, should_heal_heuristic):
        if self.heuristics.heal_selection:
            return self.heuristics.heal_selection.select(allies)
        return should_heal_heuristic.select(allies)


