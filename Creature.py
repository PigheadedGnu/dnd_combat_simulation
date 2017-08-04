from random import randint
from settings import VERBOSITY


class Creature:
    def __init__(self, name, hp, ac, proficiency, saves, actions, heuristics):
        """
        :param hp: An integer of the creatures HP
        :param ac: An integer of the creatures AC
        :param saves: A dictionary of saves with each key being a 3-letter stat code
        :param actions: A list of action objects defined in Actions.py
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
        self.heuristics = heuristics

    def take_damage(self, attack, bonus):
        damage = 0
        if attack.bonus is not None:
            hit_check = d20() + self.saves[attack.bonus] + attack.bonus_to_hit
            if hit_check >= self.ac:
                damage = calc_roll(attack) + bonus + attack.bonus_to_damage
        else:
            save_check = d20() + self.saves[attack.save['stat']]
            if save_check <= attack.save['DC']:
                damage = calc_roll(attack) + attack.bonus_to_damage

        self.hp -= damage
        if VERBOSITY > 1:
            print(self.name, "took", damage, "damage from", attack.name)

    def receive_heal(self, heal, bonus):
        health_up = calc_roll(heal) + bonus
        new_health = min(self.hp + health_up, self.max_hp)
        if VERBOSITY > 1:
            print(self.name, "healed from", self.hp, "to", new_health)
        self.hp = new_health

    @staticmethod
    def choose_action(action_set):
        for action in action_set:
            if not action.ready:
                action.try_recharge()
            if action.ready and action.num_available != 0:
                action.num_available -= 1
                action.ready = False
                return action

    def act(self, allies, enemies, heuristics):
        use_heal, ally = self._check_heal_need(allies, heuristics)
        if use_heal and [h for h in self.heals if h.num_available > 0]:
            heal = self.choose_action(self.heals)
            ally.receive_heal(heal, self.saves[heal.bonus] if heal.bonus is not "None" else 0)
        else:
            attack = self.choose_action(self.attacks)
            for _ in range(attack.multi_attack):
                target = self._choose_target(enemies, heuristics)
                target.take_damage(attack,
                                   self.saves[attack.bonus] if attack.bonus is not "None"
                                   and attack.action_type != "Spell Attack" else 0)

    def _choose_target(self, enemies, heuristics):
        enemies = [e for e in enemies if e.hp >= 0]
        if "lowest_hp" in heuristics + self.heuristics:
            min_hp = min([e.hp for e in enemies])
            target = [e for e in enemies if e.hp == min_hp][0]
        else:
            target = enemies[randint(0, len(enemies)-1)]
        return target

    def _check_heal_need(self, allies, heuristics):
        min_percent_to_heal = 0.4
        if "safe_heal" in heuristics + self.heuristics:
            min_percent_to_heal = 0.6

        for a in allies:
            if a.hp <= a.max_hp * min_percent_to_heal:
                return True, a
        return False, None


def calc_roll(action):
    """
    :param action: An action object with a dice property
    """
    total = 0
    for max_roll, num_dice in action.dice.items():
        total += sum(map(lambda x: randint(1, max_roll), range(num_dice)))
    return total


def d20():
    # Roll a d20
    return randint(1, 20)
