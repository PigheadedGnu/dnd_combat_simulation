from Actions import PhysicalAttack, SpellAttack
from effects import bleed

def short_sword_slash():
    return PhysicalAttack(name="Short Sword",
                          stat_bonus="STR",
                          save=None,
                          damage={6: 1})


def longsword_attack():
    return PhysicalAttack(name="Long Sword",
                          stat_bonus="STR",
                          save=None,
                          damage={8: 1, 6: 2})


def sneak_sword():
    return PhysicalAttack(name="Sneak Sword",
                          stat_bonus="DEX",
                          save=None,
                          damage={6: 3},
                          )


def power_throw():
    return PhysicalAttack(name="Spin Throw",
                          stat_bonus="STR",
                          save=None,
                          damage={6: 3},
                          num_available=9)


def throw_rock():
    return PhysicalAttack(name="Throw Rock",
                          stat_bonus="STR",
                          save=None,
                          damage={4: 1})


def mace_hit():
    return PhysicalAttack(name="Mace",
                          stat_bonus="STR",
                          save=None,
                          damage={8: 1})


def scorching_ray():
    return SpellAttack(name="Scorching Ray",
                       stat_bonus="INT",
                       save=None,
                       damage={6: 2},
                       num_available=2,
                       multi_attack=3)


def magic_missile():
    return SpellAttack(name="Magic Missile",
                       stat_bonus="None",
                       save=None,
                       damage={4: 1},
                       num_available=4,
                       bonus_to_hit=1000,
                       bonus_to_damage=1,
                       multi_attack=3)


def acid_splash():
    return SpellAttack(name="Acid Splash",
                       stat_bonus=None,
                       save={"stat": "DEX", "DC": 13},
                       damage={6: 1})


def sacred_flame():
    return SpellAttack(name="Sacred Flame",
                       stat_bonus=None,
                       save={"stat": "DEX", "DC": 13},
                       damage={8: 1})


def guiding_bolt():
    return SpellAttack(name="Guiding Bolt",
                       stat_bonus="WIS",
                       save=None,
                       damage={6: 4},
                       num_available=4)