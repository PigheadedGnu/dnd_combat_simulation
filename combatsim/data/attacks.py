from .effects import mace_stun
from simulator.src import damage_types
from simulator.src.actions import *


def short_sword_slash():
    return PhysicalSingleAttack(name="Short Sword",
                                serialized_name="shsw",
                                stat_bonus="STR",
                                save=None,
                                dice={6: 1},
                                damage_type=damage_types.SLASHING)


def longsword_attack():
    return PhysicalSingleAttack(name="Long Sword",
                                serialized_name="lnsw",
                                stat_bonus="STR",
                                save=None,
                                dice={8: 1, 6: 2},
                                damage_type=damage_types.SLASHING)


def sneak_sword():
    return PhysicalSingleAttack(name="Sneak Sword",
                                serialized_name="l5ss",
                                stat_bonus="DEX",
                                save=None,
                                dice={8: 1, 6: 3},
                                damage_type=damage_types.SLASHING)


def power_throw():
    return PhysicalSingleAttack(name="Spin Throw",
                                serialized_name="spth",
                                stat_bonus="STR",
                                save=None,
                                dice={6: 3},
                                num_available=9,
                                damage_type=damage_types.PIERCING)


def apm():
    return PhysicalSingleAttack(name="Armor Piercing Missile",
                                serialized_name="arpm",
                                stat_bonus="STR",
                                save=None,
                                dice={8: 5},
                                num_available=4,
                                damage_type=damage_types.PIERCING)


def throw_rock():
    return PhysicalSingleAttack(name="Throw Rock",
                                serialized_name="thrk",
                                stat_bonus="STR",
                                save=None,
                                dice={4: 1},
                                damage_type=damage_types.BLUDGEONING)


def mace_hit():
    return PhysicalSingleAttack(name="Mace Hit",
                                serialized_name="mcht",
                                stat_bonus="STR",
                                save=None,
                                dice={8: 1},
                                effects=[mace_stun()],
                                damage_type=damage_types.BLUDGEONING)


def scorching_ray():
    return SpellSingleAttack(name="Scorching Ray",
                             serialized_name="scry",
                             stat_bonus="INT",
                             save=None,
                             dice={6: 2},
                             num_available=2,
                             multi_attack=3,
                             damage_type=damage_types.FIRE)


def lightning_bolt():
    return SpellSingleAttack(name="Lightning Bolt",
                             serialized_name="lnbt",
                             save={"stat": "DEX", "DC": 15},
                             stat_bonus=None,
                             dice={6: 8},
                             num_available=3,
                             damage_type=damage_types.LIGHTNING)


def magic_missile():
    return SpellSingleAttack(name="Magic Missile",
                             serialized_name="mami",
                             stat_bonus="None",
                             save=None,
                             dice={4: 1},
                             num_available=4,
                             bonus_to_hit=1000,
                             bonus_to_damage=1,
                             multi_attack=3,
                             damage_type=damage_types.FORCE)


def acid_splash():
    return SpellSingleAttack(name="Acid Splash",
                             serialized_name="acsp",
                             stat_bonus=None,
                             save={"stat": "DEX", "DC": 13},
                             dice={6: 1},
                             damage_type=damage_types.ACID)


def sacred_flame():
    return SpellSingleAttack(name="Sacred Flame",
                             serialized_name="scfl",
                             stat_bonus=None,
                             save={"stat": "DEX", "DC": 13},
                             dice={8: 1},
                             damage_type=damage_types.RADIANT)


def guiding_bolt():
    return SpellSingleAttack(name="Guiding Bolt",
                             serialized_name="gdbt",
                             stat_bonus="WIS",
                             save=None,
                             dice={6: 4},
                             num_available=4,
                             damage_type=damage_types.RADIANT)


def beak():
    return PhysicalSingleAttack(name="Beak Strike",
                                serialized_name="bksk",
                                stat_bonus="STR",
                                dice={8: 1},
                                damage_type=damage_types.PIERCING)


def claw():
    return PhysicalSingleAttack(name="Claw Strike",
                                serialized_name="clsk",
                                stat_bonus="STR",
                                dice={6: 2},
                                damage_type=damage_types.SLASHING)


def griffon_combo():
    return ComboAttack(name="Griffon Combo",
                       serialized_name="grcm",
                       attacks=[beak(), claw()])