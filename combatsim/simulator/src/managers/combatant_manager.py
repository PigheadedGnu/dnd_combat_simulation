from .action_manager import ActionManager
from ..combatant import Combatant
from ..utils import *


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

    def get_all_combatants(self):
        """ Used to populate the combatants on the front-end """
        return_info = []
        for combatant in self.combatant_info:
            c_info = self.combatant_info[combatant]
            return_info.append({
                "label": capitalize(c_info['name']),
                "value": c_info['name'],
                "cr": c_info['cr'] if 'cr' in c_info else None,
                "expDamage": 10,
                "creatureType": c_info['creature_type'] if "creature_type" in c_info else None
            })

        return return_info
