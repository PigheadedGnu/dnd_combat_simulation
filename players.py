from creature import Creature
from attacks import *
from heals import *


def Marshall():
    return Creature(name="Marshall", hp=27, ac=18, proficiency=2,
                    saves={"STR": 2, "CON": 2, "DEX": 1, "INT": 1, "WIS": 2, "CHA": 1},
                    actions=[guiding_bolt(), mace_hit(), cure_wounds()])


def Max():
    return Creature(name="Max", hp=24, ac=13, proficiency=2,
                    saves={"STR": 2, "CON": 2, "DEX": 2, "INT": 2, "WIS": 2, "CHA": 2},
                    actions=[scorching_ray(), magic_missile(), acid_splash()])


def Johnny():
    return Creature(name="Johnny", hp=25, ac=14, proficiency=2,
                    saves={"STR": 1, "CON": 1, "DEX": 2, "INT": 2, "WIS": 2, "CHA": 2},
                    actions=[sneak_sword()])


def Freddy():
    return Creature(name="Freddy", hp=25, ac=14, proficiency=2,
                    saves={"STR": 3, "CON": 1, "DEX": 2, "INT": 2, "WIS": 2, "CHA": 2},
                    actions=[power_throw(), throw_rock()])
