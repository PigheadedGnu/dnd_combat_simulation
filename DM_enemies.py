from Creature import Creature
from attacks import *


def roper_bite():
    return PhysicalAttack(name="Bite",
                          stat_bonus="STR",
                          save=None,
                          damage={8: 3})


def roper():
    return Creature(name="Roper", hp=93, ac=19, proficiency=3,
                    saves={"STR": 4, "CON": 3, "DEX": -1, "INT": 1, "WIS": 1, "CHA": 1},
                    actions=[roper_bite()], heuristics=[])
