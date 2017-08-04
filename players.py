from Creature import Creature
from attacks import *
from heals import *


def Marshall():
    return Creature(name="Marshall", hp=20, ac=18, proficiency=2,
                    saves={"STR": 2, "CON": 2, "DEX": 2, "INT": 2, "WIS": 2, "CHA": 2},
                    actions=[mace_hit, cure_wounds], heuristics=[])
