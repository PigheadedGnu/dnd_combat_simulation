from random import random


class Action:
    action_type = ""
    recharge_percentile = 0.0
    ready = True
    bonus = "None"

    def try_recharge(self):
        percentile = random()
        if percentile >= self.recharge_percentile:
            self.ready = True


class Attack(Action):
    def __init__(self, name, stat_bonus, save, damage,
                 recharge_percentile=0.0, num_available=-1, bonus_to_hit=0,
                 bonus_to_damage=0, multi_attack=1):
        """
        :param stat_bonus: A 3-letter stat code that is used to get the bonus for to-hit and
         damage
        :param save: A dictionary with an entry for the stat (a 3-letter stat code) and an entry
         for the DC, which is an integer.
        :param damage: A dictionary of damage dice. The key is the integer of the maximum face of
         the dice and the value is the number of dice. E.g. {8: 6} would be 6d8 damage
        :param recharge_percentile: Percentile to recharge the attack. Randomly generate percentile
         after each use and on each subsequent turn and if randomly generated percentile is greater
         than the attack is ready for use.
        :param num_available: Number of times this attack can be used in a battle
        :param bonus_to_hit: Bonus to hit of the attack added to the d20
        :param bonus_to_damage: Bonus to damage of the attack, added to the attack roll.
        :param multi_attack: How many times the attack dice should be rolled for a single
         attack action
        """
        assert stat_bonus is None or save is None
        self.name = name
        self.bonus = stat_bonus
        self.save = save
        self.dice = damage
        self.recharge_percentile = recharge_percentile
        self.num_available = num_available
        self.bonus_to_hit = bonus_to_hit
        self.bonus_to_damage = bonus_to_damage
        self.multi_attack = multi_attack
        self.ready = True  # If the attack is ready at the current time. All attacks start ready
        self.action_type = "Attack"


class SpellAttack(Attack):
    def __init__(self, **kwargs):
        super(SpellAttack, self).__init__(**kwargs)
        self.action_type = "Spell Attack"


class Heal(Action):
    def __init__(self, name, heal, stat_bonus, recharge_percentile, num_available):
        self.name = name
        self.dice = heal
        self.bonus = stat_bonus
        self.recharge_percentile = recharge_percentile
        self.num_available = num_available
        self.ready = True  # If the attack is ready at the current time. All attacks start ready
        self.action_type = "Heal"

