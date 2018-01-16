from heuristics.HeuristicContainer import *

from data.attacks import *
from src.combatant import Combatant
from src.heuristics.target_selection_heuristics import *


def roper_bite():
    return PhysicalSingleAttack(name="Bite",
                                stat_bonus="STR",
                                save=None,
                                damage={8: 3})


def roper():
    return Combatant(name="Roper", hp=74, ac=18, proficiency=3,
                     saves={"STR": 4, "CON": 3, "DEX": -1, "INT": 1, "WIS": 1, "CHA": 1},
                     actions=[roper_bite()], heuristics=[])


def wounding_ray():
    return SpellSave(name="Wounding Ray",
                     stat_bonus="INT",
                     save={"stat": "CON", "DC": 13},
                     damage={10: 3})


def two_headed_spectator():
    return Combatant(name="Spectator x 2", hp=59, ac=15, proficiency=3,
                     saves={"STR": 4, "CON": 3, "DEX": -1, "INT": 1, "WIS": 1, "CHA": 1},
                     actions=[short_sword_slash()], heuristics=[])


def poison_breath():
    return SpellSingleAttack(name="Poison Breath",
                             stat_bonus=None,
                             save={"stat": "CON", "DC": 14},
                             damage={6: 8},
                             multi_attack=3,
                             aoe=True,
                             recharge_percentile=0.833)


def clawclawbite():
    return PhysicalSingleAttack(name="claw claw bite",
                                stat_bonus="STR",
                                save=None,
                                damage={6: 2},
                                bonus_to_damage=4,
                                bonus_to_hit=0,
                                multi_attack=4)


def green_dragon():
    return Combatant(name="Coazoith", hp=136, ac=18, proficiency=3,
                     saves={"STR": 4, "CON": 6, "DEX": 4, "INT": 3, "WIS": 4, "CHA": 5},
                     actions=[poison_breath(), clawclawbite()],
                     heuristics=HeuristicContainer(attack_selection=LowestHealth()))
