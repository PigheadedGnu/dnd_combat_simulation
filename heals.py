from actions import Heal


def cure_wounds():
    return Heal(name="Cure Wounds", heal={8: 1}, stat_bonus="WIS",
                recharge_percentile=0.0, num_available=3)