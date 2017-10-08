from random import random
from copy import deepcopy
import math

from utils import calc_roll, d20
from logger import Logger


class Action:
    name = ""
    action_type = ""
    recharge_percentile = 0.0
    ready = True
    stat_bonus = "None"
    logger = Logger()

    def try_recharge(self):
        percentile = random()
        if percentile >= self.recharge_percentile:
            self.ready = True


class Attack(Action):
    def __init__(self, name, stat_bonus, save, damage,
                 recharge_percentile=0.0, num_available=-1, bonus_to_hit=0,
                 bonus_to_damage=0, multi_attack=1, aoe=False, effects=None):
        """
        :param name: Name of the attack
        :param stat_bonus: bonus to hit for the attack. One of this or
                            save must be None
        :param save: a dictionary with 'stat' and 'DC' as entries. One of this
                        or stat_bonus must be None
        :param damage: dictionary of damage dice for the attack
        :param recharge_percentile: percentile for recharge on the attack. The
                                        chance to recharge is
                                        p = (1 - recharge_percentile)
        :param num_available: number of times this is available per battle
        :param bonus_to_hit: integer for bonus to hit for the attack
        :param bonus_to_damage: integer for bonus to damage on the attack
        :param multi_attack: number of targets to hit for this attack
        :param effects: list of any Effect objects the attack inflicts
        """
        assert stat_bonus is None or save is None
        self.name = name
        self.stat_bonus = stat_bonus
        self.save = save
        self.dice = damage
        self.recharge_percentile = recharge_percentile
        self.num_available = num_available
        self.bonus_to_hit = bonus_to_hit
        self.bonus_to_damage = bonus_to_damage
        self.multi_attack = multi_attack
        self.ready = True  # If the attack is ready at the current time. All attacks start ready
        self.action_type = "Attack"
        self.aoe = aoe
        self.effects = effects if effects else []

    def do_damage(self, attacker, target):
        raise NotImplementedError("do_damage is not implemented on this class!")

    def apply_effects(self, target):
        [target.applied_effects.append(deepcopy(effect)) for effect in self.effects]

    def log_attack(self, attacker, target, damage):
        self.logger.log_action("{0} took {1} damage from {2} ({3})".format(target.name, damage, self.name, attacker.name))


class PhysicalAttack(Attack):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_damage(self, attacker, target):
        damage = 0
        hit_check = d20() + attacker.saves[self.stat_bonus] + self.bonus_to_hit
        if hit_check >= target.ac:
            damage = calc_roll(self.dice) + attacker.saves[self.stat_bonus] + self.bonus_to_damage

        target.hp -= damage
        self.log_attack(attacker, target, damage)


class SpellAttack(Attack):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_damage(self, attacker, target):
        damage = 0
        if self.stat_bonus is not None:
            attack_bonus = attacker.proficiency + \
                           attacker.saves[self.stat_bonus] if self.stat_bonus != "None" else 0
            hit_check = d20() + attack_bonus + self.bonus_to_hit
            if hit_check >= attacker.ac:
                damage = calc_roll(self.dice) + self.bonus_to_damage
        else:
            save_check = d20() + target.saves[self.save['stat']]
            if save_check <= self.save['DC']:
                damage = calc_roll(self.dice) + self.bonus_to_damage

        target.hp -= damage
        self.log_attack(attacker, target, damage)


class SpellSave(Attack):
    def __init__(self, **kwargs):
        assert kwargs.get('save') is not None
        super().__init__(**kwargs)

    def do_damage(self, attacker, target):
        save_check = d20() + target.saves[self.save['stat']]
        damage = calc_roll(self.dice)
        if save_check > self.save['DC']:
            damage = math.ceil(damage / 2.0)

        target.hp -= damage

        self.log_attack(attacker, target, damage)


class Heal(Action):
    def __init__(self, name, heal, stat_bonus, recharge_percentile, num_available):
        self.name = name
        self.dice = heal
        self.stat_bonus = stat_bonus
        self.recharge_percentile = recharge_percentile
        self.num_available = num_available
        self.ready = True  # If the attack is ready at the current time. All attacks start ready
        self.action_type = "Heal"

    def log_heal(self, healed, new_health, healer):
        self.logger.log_action("{0} healed from {1} to {2} ({3})".format(healed.name, healed.hp, new_health, healer.name))

    def do_heal(self, healer, healed):
        health_up = calc_roll(self.dice) + (healer.saves[self.stat_bonus] if
                                       self.stat_bonus != "None" else 0)
        new_health = min(healed.hp + health_up, healed.max_hp)
        self.log_heal(healed, new_health, healer)
        healed.hp = new_health

