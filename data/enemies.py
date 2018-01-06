from heuristics.HeuristicContainer import HeuristicContainer

from data.attacks import *
from src.creature import Creature
from src.heuristics.target_selection_heuristics import *


def goblin():
    return Creature(name="Goblin", hp=7, ac=14, proficiency=1,
                    saves={"STR": 1, "CON": 1, "DEX": 1, "INT": 1, "WIS": 1, "CHA": 1},
                    actions=[short_sword_slash()],
                    heuristics=HeuristicContainer(attack_selection=HighestAC()))


def hobgoblin():
    return Creature(name="Hobgoblin", hp=11, ac=18, proficiency=2,
                    saves={"STR": 1, "CON": 1, "DEX": 1, "INT": 1, "WIS": 1, "CHA": 1},
                    actions=[longsword_attack()])


def griffon():
    return Creature(name="Griffon", hp=59, ac=12, proficiency=2,
                    saves={"STR": 4, "CON": 3, "DEX": 2, "INT": -4, "WIS": 1, "CHA": -1},
                    actions=[griffon_combo()])






