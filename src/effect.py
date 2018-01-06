from src.debug.logger import Logger
from src.utils import d20, calc_roll


class Effect:
    logger = Logger()

    def __init__(self, turns, name):
        self.turns_left = turns
        self.name = name

    def apply(self, creature):
        """ How does this affect get applied """
        raise RuntimeError("apply() is not implemented for {}!".format(self.name))

    def on_turn_start(self, creature):
        """ What this effect does at the start of a turn """
        raise RuntimeError("on_turn_start() is not implemented for {}!".format(self.name))

    def on_turn_end(self, creature):
        """ What this effect does at the end of a turn.

            This method should implement some way for the effect to be removed.
        """
        raise RuntimeError("on_turn_end() is not implemented for {}!".format(self.name))

    def jsonify(self):
        effect_info = {
            "Effect Name": self.name,
            "Maximum Turns": self.turns_left,
        }
        return effect_info


class DOTEffect(Effect):
    def __init__(self, dice, save, turns, name):
        """ DOT effect applies damage each turn the effect is active

        :param dice: A dictionary of (faces, amount) pairs
        :param save: A dictionary with 'stat' and 'DC' entries
        :param turns: Number of turns this stays active
        :param name: Name of the effect
        """

        super().__init__(turns, name)
        self.save = save
        self.dice = dice

    def apply(self, creature):
        save_attempt = d20() + creature.saves[self.save['stat']]
        if save_attempt >= self.save['DC']:
            self.logger.log_action(
                "{0} saved from {1}".format(creature.name, self.name))
            return
        else:
            creature.applied_effects.append(self)

    def on_turn_start(self, creature):
        total = calc_roll(self.dice)
        self.logger.log_action("{0} suffered {1} for {2} damage".format(creature.name, self.name, total))
        creature.hp -= total
        self.turns_left -= 1

    def on_turn_end(self, creature):
        save_attempt = d20() + creature.saves[self.save['stat']]
        if save_attempt >= self.save['DC']:
            self.logger.log_action(
                "{0} saved from {1}".format(creature.name, self.name))
            return False
        else:
            self.logger.log_action(
                "{0} failed to save from {1}".format(creature.name, self.name))
            return True

    def jsonify(self):
        effect_info = super().jsonify()
        effect_info['Damage Dice'] = self.dice
        effect_info['Save'] = self.save
        return effect_info


class StunEffect(Effect):
    def __init__(self, save, turns, name):
        """ Stun effect takes away the sufferer's actions for each turn its active

        :param save: A dictionary with 'stat' and 'DC' entries
        :param turns: Number of turns this stays active
        :param name: Name of this effect
        """
        super().__init__(turns, name)
        self.save = save

    def apply(self, creature):
        save_attempt = d20() + creature.saves[self.save['stat']]
        if save_attempt >= self.save['DC']:
            self.logger.log_action(
                "{0} saved from {1}".format(creature.name, self.name))
            return
        else:
            creature.applied_effects.append(self)

    def on_turn_start(self, creature):
        creature.num_actions_available = 0
        self.logger.log_action(
            "{0} was stunned by {1}".format(creature.name, self.name))
        self.turns_left -= 1

    def on_turn_end(self, creature):
        if self.turns_left <= 0:
            return False

        save_attempt = d20() + creature.saves[self.save['stat']]
        if save_attempt >= self.save['DC']:
            self.logger.log_action(
                "{0} saved from {1}".format(creature.name, self.name))
            return False
        else:
            self.logger.log_action(
                "{0} failed to save from {1}".format(creature.name, self.name))
            return True

    def jsonify(self):
        effect_info = super().jsonify()
        effect_info['Save'] = self.save
        return effect_info