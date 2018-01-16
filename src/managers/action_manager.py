from src.actions import ComboAttack, Heal, SpellSave, SpellSingleAttack, \
    PhysicalSingleAttack
from src.managers.effect_manager import EffectManager
from settings import BASE_DIR
import json

ACTION_MAPPING = {"Combo Attack": ComboAttack,
                  "Heal": Heal,
                  "Spell Attack Requiring Save": SpellSave,
                  "Single Target Spell Attack": SpellSingleAttack,
                  "Single Target Physical Attack": PhysicalSingleAttack}


class ActionManager:
    def __init__(self):
        with open(BASE_DIR + '/data/actions.json', 'r') as f:
            self.action_info = json.load(f)
        self.effect_manager = EffectManager()

    def load_action(self, action_name):
        try:
            info = self.action_info[action_name]
        except KeyError:
            raise RuntimeError("Action with name {0} "
                               "could not be found.".format(action_name))

        action_effects = []
        for effect_name in info['effects']:
            action_effects.append(self.effect_manager.load_effect(effect_name))

        build_action_info = {k: v for k, v in info.items()
                             if k not in ['effects', 'action_type']}

        return ACTION_MAPPING[info['action_type']](effects=action_effects,
                                                   **build_action_info)
