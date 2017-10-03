from logger import Logger
from utils import *


class Effect:
    logger = Logger()

    def __init__(self, turns, name):
        self.turns_left = turns
        self.name = name


class DOTEffect(Effect):
    def __init__(self, dice, turns, name):
        super().__init__(turns, name)
        self.dice = dice

    def apply(self, creature):
        total = calc_roll(self.dice)
        self.logger.log_action("{0} suffered {1} for {2} damage".format(creature.name, self.name, total))
        creature.hp -= total
        self.turns_left -= 1
