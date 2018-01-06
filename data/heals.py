from src.actions import Heal


def cure_wounds():
    return Heal(name="Cure Wounds", heal={8: 1}, stat_bonus="WIS",
                recharge_percentile=0.0, num_available=3)


def prayer_of_healing():
    return Heal(name="Prayer of Healing", heal={8: 2}, stat_bonus="WIS",
                recharge_percentile=0.0, num_available=3, num_targets=4)


def channel_divinity():
    return Heal(name="Divine Heal", heal={1: 10}, stat_bonus="WIS",
                recharge_percentile=0.0, num_available=2, num_targets=2)