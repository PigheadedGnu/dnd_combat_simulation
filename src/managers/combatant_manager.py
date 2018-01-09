from src.combatant import Combatant
from src.managers.action_manager import ActionManager
from settings import BASE_DIR
import json


class CombatantManager:
    def __init__(self):
        with open(BASE_DIR + '/data/combatants.json', 'r') as f:
            self.combatant_info = json.load(f)
        self.action_manager = ActionManager()

    def load_combatant(self, combatant_name):
        try:
            info = self.combatant_info[combatant_name]
        except KeyError:
            raise RuntimeError('Creature with name {0} could not '
                               'be found.'.format(combatant_name))

        combatant_actions = []
        for action_name in info['actions']:
            combatant_actions.append(self.action_manager.load_action(action_name))

        build_combatant_info = {k: v for k, v in info.items() if k != 'actions'}

        return Combatant(actions=combatant_actions, **build_combatant_info)
