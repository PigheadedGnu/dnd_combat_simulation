from simulator.src.actions import Heal


def cure_wounds():
    return Heal(name="Cure Wounds",
                serialized_name='cwnd',
                dice={8: 1}, stat_bonus="WIS",
                recharge_percentile=0.0, num_available=3)


def prayer_of_healing():
    return Heal(name="Prayer of Healing",
                serialized_name="proh",
                dice={8: 2}, stat_bonus="WIS",
                recharge_percentile=0.0, num_available=3, num_targets=4)


def channel_divinity():
    return Heal(name="Divine Heal",
                serialized_name="dvhl",
                dice={10: 1}, stat_bonus="WIS",
                recharge_percentile=0.0, num_available=2, num_targets=2)
