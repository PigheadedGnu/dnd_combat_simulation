from effects.effect import *


def bleed(dice, turns):
    return DOTEffect(dice=dice, turns=turns, name="bleed")
