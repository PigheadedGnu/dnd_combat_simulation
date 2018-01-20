import math
from random import random

from .utils import *

from .debug.logger import Logger


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
    def __init__(self, name, recharge_percentile=0.0, num_available=-1,
                 multi_attack=1):
        self.name = name
        self.recharge_percentile = recharge_percentile
        self.num_available = num_available
        self.action_type = "Attack"
        self.multi_attack = multi_attack
        self.aoe = False
        self.ready = True  # If the attack is ready at the current time. All attacks start ready


class SingleAttack(Attack):
    def __init__(self, dice, damage_type, bonus_to_hit=0, bonus_to_damage=0,
                 stat_bonus=None, save=None, aoe=False, effects=None, **kwargs):
        """
        :param name: Name of the attack
        :param stat_bonus: bonus to hit for the attack. One of this or
                            save must be None
        :param save: a dictionary with 'stat' and 'DC' as entries. One of this
                        or stat_bonus must be None
        :param dice: dictionary of damage dice for the attack
        :param recharge_percentile: percentile for recharge on the attack. The
                                        chance to recharge is
                                        p = (1 - recharge_percentile)
        :param num_available: number of times this is available per battle
        :param bonus_to_hit: integer for bonus to hit for the attack
        :param bonus_to_damage: integer for bonus to damage on the attack
        :param multi_attack: number of targets to hit for this attack
        :param aoe: If this is an aoe attack or not. If it is, the multi-attack
                    should be >1 and the attack will not hit the same target twice
        :param effects: list of any Effect objects the attack inflicts
        """
        assert stat_bonus is None or save is None
        assert stat_bonus is not None or save is not None
        self.stat_bonus = stat_bonus
        self.damage_type = damage_type
        self.save = save
        self.dice = load_dice(dice)
        self.bonus_to_hit = bonus_to_hit
        self.bonus_to_damage = bonus_to_damage
        self.aoe = aoe
        self.effects = effects if effects else []

        super().__init__(**kwargs)

    def do_damage(self, attacker, target):
        """ Called to test whether an attack hits and then applies the damage.
        :param attacker: The creature using the attack
        :param target: The creature receiving the attack
        :return: None, damage is applied on the target object
        """
        raise NotImplementedError("do_damage is not implemented on this class!")

    def calc_expected_damage(self):
        return self.multi_attack * sum([n_dice * (max_roll / 2.0 + 0.5) for
                                        n_dice, max_roll in self.dice.items()])

    def apply_effects(self, target):
        [effect.apply(target) for effect in self.effects]

    def log_attack(self, attacker, target, damage):
        self.logger.log_action("{0} took {1} damage from {2} ({3})".format(
            target.name, damage, self.name, attacker.name))

    def jsonify(self, attack_type="Single Target Attack", write_to_file=True):
        attack_info = {
            "name": self.name,
            "action_type": attack_type,
            "damage_type": self.damage_type,
            "stat_bonus": self.stat_bonus,
            "save": self.save,
            "dice": self.dice,
            "bonus_to_hit": self.bonus_to_hit,
            "bonus_to_damage": self.bonus_to_damage,
            "aoe": self.aoe,
            "multi_attack": self.multi_attack,
            "recharge_percentile": self.recharge_percentile,
            "effects": [e.name for e in self.effects]
        }
        if write_to_file:
            write_json_to_file("actions.json", attack_info)
        return attack_info


class PhysicalSingleAttack(SingleAttack):
    def __init__(self, **kwargs):
        """ An attack that tests the chance to hit against target's AC
        Chance to hit = roll d20 + attackers save + attack bonus to hit
        """
        super().__init__(**kwargs)

    def do_damage(self, attacker, target):
        damage = 0
        hit_check = d20() + attacker.saves[self.stat_bonus] + self.bonus_to_hit
        if hit_check >= target.ac:
            damage = calc_roll(self.dice) + attacker.saves[self.stat_bonus] + self.bonus_to_damage

        target.take_damage(damage, self.damage_type)
        self.log_attack(attacker, target, damage)

    def jsonify(self):
        return super().jsonify("Single Target Physical Attack")


class SpellSingleAttack(SingleAttack):
    def __init__(self, **kwargs):
        """ Either a saving throw from target or test of hit chance to targets AC
        Chance to hit is d20 + relevant stat bonus + bonus to damage
        A saving throw is a d20 + relevant stat bonus compared to spell DC
        """
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

        target.take_damage(damage, self.damage_type)
        self.log_attack(attacker, target, damage)

    def jsonify(self):
        return super().jsonify("Single Target Spell Attack")


class SpellSave(SingleAttack):
    """ Spell saves are attacks which do full damage on a failed save or half
    as much on a successful save.

    :param name: Name of the attack
    :param stat_bonus: Must be None
    :param save: a dictionary with 'stat' and 'DC' as entries.
    :param damage: dictionary of damage dice for the attack
    :param recharge_percentile: percentile for recharge on the attack. The
                                    chance to recharge is
                                    p = (1 - recharge_percentile)
    :param num_available: number of times this is available per battle
    :param bonus_to_hit: Should be None
    :param bonus_to_damage: Should be None
    :param multi_attack: number of targets to hit for this attack.
                        (Expected number if aoe)
    :param effects: list of any Effect objects the attack inflicts
    """
    def __init__(self, **kwargs):
        assert kwargs.get('save') is not None
        super().__init__(**kwargs)

    def do_damage(self, attacker, target):
        save_check = d20() + target.saves[self.save['stat']]
        damage = calc_roll(self.dice)
        if save_check > self.save['DC']:
            damage = math.ceil(damage / 2.0)

        target.take_damage(damage, self.damage_type)

        self.log_attack(attacker, target, damage)

    def jsonify(self):
        return super().jsonify("Spell Attack Requiring Save")


class Heal(Action):
    def __init__(self, name, dice, stat_bonus, recharge_percentile=0.0,
                 num_available=-1, num_targets=1, effects=None):
        """ A heal restores hit points to an ally. Always hits

        :param name: string that is name of the heal
        :param heal: dictionary with keys as dice value and values as number of that dice
        :param stat_bonus: string with the bonus based of which stat the caster uses
        :param recharge_percentile: chance to recharge is p = 1 - recharge percentile
        :param num_available: number of this heal available during a battle.
                            a value of -1 means it's always available.
        """
        self.name = name
        self.dice = load_dice(dice)
        self.stat_bonus = stat_bonus
        self.recharge_percentile = recharge_percentile
        self.num_available = num_available
        self.ready = True  # If the attack is ready at the current time. All attacks start ready
        self.action_type = "Heal"
        self.num_targets = num_targets
        self.effects = effects if effects else []

    def log_heal(self, healed, new_health, healer):
        self.logger.log_action("{0} healed from {1} to {2} ({3})".format(healed.name, healed.hp, new_health, healer.name))

    def do_heal(self, healer, healed):
        health_up = calc_roll(self.dice) + (healer.saves[self.stat_bonus] if
                                       self.stat_bonus != "None" else 0)
        new_health = min(healed.hp + health_up, healed.max_hp)
        self.log_heal(healed, new_health, healer)
        healed.hp = new_health

    def jsonify(self, write_to_file=True):
        heal_info = {
            "action_type": "Heal",
            "name": self.name,
            "dice": self.dice,
            "stat_bonus": self.stat_bonus,
            "recharge_percentile": self.recharge_percentile,
            "num_targets": self.num_targets,
            "effects": [e.name for e in self.effects]
        }
        if write_to_file:
            write_json_to_file("actions.json", heal_info)
        return heal_info


class ComboAttack(Attack):
    def __init__(self, attacks, **kwargs):
        """ Container for multiple different attacks that do different damage

        This differs from a single attack multiattack, where each hit does the
        same damage dice, because this can incorporate multiple attacks of
        different types against a single enemy.

        An example of this is a Griffon which does two attacks every turn, one
        with it's beak and one with it's claws. Beak does 1d8+4 damage and claws
        do 2d6+4 damage.

        :param attacks: List of attack actions

        Notable keyword args:
        :param multi_attack: Does it perform the combo on multiple enemeies?
                            a value of 1 typically makes the most sense.

        """
        for a in attacks:
            assert isinstance(a, SingleAttack)
        self.attacks = attacks

        super().__init__(**kwargs)

    def calc_expected_damage(self):
        total_expected_damage = 0
        for attack in self.attacks:
            total_expected_damage += attack.calc_expected_damage()
        return total_expected_damage

    def do_damage(self, attacker, target):
        for attack in self.attacks:
            attack.do_damage(attacker, target)

    def apply_effects(self, target):
        for attack in self.attacks:
            attack.apply_effects(target)

    def jsonify(self, write_to_file=True):
        attack_info = {
            "action_type": "Combo Attack",
            "attacks": [a.jsonify() for a in self.attacks]
        }
        if write_to_file:
            write_json_to_file('actions.json', attack_info)
        return attack_info
