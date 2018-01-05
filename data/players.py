from data.attacks import *
from data.heals import *
from src.creature import Creature


def Marshall():
    return Creature(name="Marshall", hp=42, ac=18, proficiency=3,
                    saves={"STR": 2, "CON": 2, "DEX": 1, "INT": 1, "WIS": 2, "CHA": 1},
                    actions=[guiding_bolt(), mace_hit(), cure_wounds(), channel_divinity(), prayer_of_healing()])


def Max():
    return Creature(name="Max", hp=32, ac=11, proficiency=3,
                    saves={"STR": 2, "CON": 2, "DEX": 2, "INT": 2, "WIS": 2, "CHA": 2},
                    actions=[lightning_bolt(), scorching_ray(), magic_missile(), acid_splash()])


def Johnny():
    return Creature(name="Johnny", hp=40, ac=14, proficiency=3,
                    saves={"STR": 1, "CON": 1, "DEX": 2, "INT": 2, "WIS": 2, "CHA": 2},
                    actions=[sneak_sword()])


def Freddy():
    return Creature(name="Freddy", hp=38, ac=14, proficiency=3,
                    saves={"STR": 4, "CON": 1, "DEX": 2, "INT": 2, "WIS": 2, "CHA": 2},
                    actions=[power_throw(), throw_rock(), apm()])
