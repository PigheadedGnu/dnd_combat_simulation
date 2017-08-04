from random import random, randint
from Creature import d20
from settings import VERBOSITY


class Action:
    name = ""
    action_type = ""
    recharge_percentile = 0.0
    ready = True
    stat_bonus = "None"

    def try_recharge(self):
        percentile = random()
        if percentile >= self.recharge_percentile:
            self.ready = True


class Attack(Action):
    def __init__(self, name, stat_bonus, save, damage,
                 recharge_percentile=0.0, num_available=-1, bonus_to_hit=0,
                 bonus_to_damage=0, multi_attack=1):
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

    def do_damage(self, attacker, target):
        raise NotImplementedError("do_damage is not implemented on this class!")


class PhysicalAttack(Attack):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_damage(self, attacker, target):
        damage = 0
        hit_check = d20() + attacker.saves[self.stat_bonus] + self.bonus_to_hit
        if hit_check >= target.ac:
            damage = calc_roll(self) + attacker.saves[self.stat_bonus] + self.bonus_to_damage

        target.hp -= damage
        if VERBOSITY > 1:
            print(target.name, "took", damage, "damage from", attacker.name,
                  "({0})".format(self.name))


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
                damage = calc_roll(self) + self.bonus_to_damage
        else:
            save_check = d20() + target.saves[self.save['stat']]
            if save_check <= self.save['DC']:
                damage = calc_roll(self) + self.bonus_to_damage

        target.hp -= damage
        if VERBOSITY > 1:
            print(target.name, "took", damage, "damage from", attacker.name,
                  "({0})".format(self.name))


class Heal(Action):
    def __init__(self, name, heal, stat_bonus, recharge_percentile, num_available):
        self.name = name
        self.dice = heal
        self.stat_bonus = stat_bonus
        self.recharge_percentile = recharge_percentile
        self.num_available = num_available
        self.ready = True  # If the attack is ready at the current time. All attacks start ready
        self.action_type = "Heal"

    def do_heal(self, healer, healed):
        health_up = calc_roll(self) + (healer.saves[self.stat_bonus] if
                                       self.stat_bonus != "None" else 0)
        new_health = min(healed.hp + health_up, healed.max_hp)
        if VERBOSITY > 1:
            print(healed.name, "healed from", healed.hp, "to", new_health)
        healed.hp = new_health


def calc_roll(action):
    """
    :param action: An action object with a dice property
    """
    total = 0
    for max_roll, num_dice in action.dice.items():
        total += sum(map(lambda x: randint(1, max_roll), range(num_dice)))
    return total
