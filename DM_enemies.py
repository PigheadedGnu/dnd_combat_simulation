from creature import Creature
from attacks import *
from actions import *


def roper_bite():
    return PhysicalAttack(name="Bite",
                          stat_bonus="STR",
                          save=None,
                          damage={8: 3})


def roper():
    return Creature(name="Roper", hp=74, ac=18, proficiency=3,
                    saves={"STR": 4, "CON": 3, "DEX": -1, "INT": 1, "WIS": 1, "CHA": 1},
                    actions=[roper_bite()], heuristics=[])


def wounding_ray():
    return SpellSave(name="Wounding Ray",
                     stat_bonus="INT",
                     save={"stat": "CON", "DC": 13},
                     damage={10: 3})


def two_headed_spectator():
    return Creature(name="Spectator x 2", hp=59, ac=15, proficiency=3,
                    saves={"STR": 4, "CON": 3, "DEX": -1, "INT": 1, "WIS": 1, "CHA": 1},
                    actions=[short_sword_slash()], heuristics=[])