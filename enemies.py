from Creature import Creature
from attacks import *


def goblin():
    return Creature(name="Goblin", hp=7, ac=14, proficiency=1,
                    saves={"STR": 1, "CON": 1, "DEX": 1, "INT": 1, "WIS": 1, "CHA": 1},
                    actions=[short_sword_slash()], heuristics=[])


def hobgoblin():
    return Creature(name="Hobgoblin", hp=11, ac=18, proficiency=2,
                    saves={"STR": 1, "CON": 1, "DEX": 1, "INT": 1, "WIS": 1, "CHA": 1},
                    actions=[longsword_attack()], heuristics=[])






