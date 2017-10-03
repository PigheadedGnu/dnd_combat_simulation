from effects.effect import *


def bleed(dice, save, turns):
    return DOTEffect(dice=dice, save=save, turns=turns, name="bleed")


def mace_stun():
    return StunEffect(save={'stat': 'CON', 'DC': 14}, turns=3, name="mace_stun")