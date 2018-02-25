from simulator.src.utils import *
from simulator.src.debug.logger import Logger


class Effect:
    logger = Logger()

    def __init__(self, max_turns, name):
        self.turns_left = max_turns
        self.name = name
        self.effect_type = "Base Effect"

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

    def jsonify(self, effect_info=None, write_to_file=True):
        if not effect_info:
            effect_info = {
                "name": self.name,
                "max_turns": self.turns_left,
                "effect_type": self.effect_type
            }
        else:
            effect_info['name'] = self.name
            effect_info['max_turns'] = self.turns_left
            effect_info['effect_type'] = self.effect_type

        if write_to_file:
            write_json_to_file('effects.json', effect_info)
        return effect_info


class DOTEffect(Effect):
    def __init__(self, dice, save, max_turns, name):
        """ DOT effect applies damage each turn the effect is active

        :param dice: A dictionary of (faces, amount) pairs
        :param save: A dictionary with 'stat' and 'DC' entries
        :param max_turns: Number of turns this stays active
        :param name: Name of the effect
        """

        super().__init__(max_turns, name)
        self.save = save
        self.dice = load_dice(dice)
        self.effect_type = "DOT Effect"

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

    def jsonify(self, effect_info=None, write_to_file=True):
        if not effect_info:
            effect_info = {
                'dice': self.dice,
                'save': self.save
            }
        else:
            effect_info['dice'] = self.dice
            effect_info['save'] = self.save
        return super().jsonify(effect_info, write_to_file)


class StunEffect(Effect):
    def __init__(self, save, max_turns, name):
        """ Stun effect takes away the sufferer's actions for each turn its active

        :param save: A dictionary with 'stat' and 'DC' entries
        :param max_turns: Number of turns this stays active
        :param name: Name of this effect
        """
        super().__init__(max_turns, name)
        self.save = save
        self.effect_type = "Stun Effect"

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

    def jsonify(self, effect_info=None, write_to_file=True):
        if not effect_info:
            effect_info = {
                'save': self.save
            }
        else:
            effect_info['save'] = self.save
        return super().jsonify(effect_info, write_to_file)


class PermanentTypeResistance(Effect):
    def __init__(self, max_turns, name):
        """ PermanentTypeResistance specifies that the thing with this effect is
             resistant to any damage from the named given type permanently

        :param max_turns: Number of turns this stays active
        :param name: Name of the element that this type is resistant to
        """
        super().__init__(max_turns, name)
        self.effect_type = "Type Resistance"

    def apply(self, creature):
        creature.applied_effects.append(self)

    def on_turn_start(self, creature):
        pass

    def on_turn_end(self, creature):
        return True

    def jsonify(self, effect_info=None, write_to_file=True):
        return super().jsonify(effect_info, write_to_file)
