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

    def deserialize_combatant(self, serialized_combatant):
        """ Takes a string of the below format and turns it into a combatant

        String form:
            ?<name>:<hp>:<ac>:<proficiency>:<str save>:<dex save>:<con save>:
            <wis save>:<int save>:<cha save>?[action...]?[effect...]

        Name is a string and every other element besides actions and effects
            are integers.
        [action...] is a list of actions separated by |s
            Only support 4-char action short-names now.
        [effect...] is a list of effects separated by |s

        Return:
            combatant: A combatant built from the given string
        """
        split_string = serialized_combatant.split("?")[1:]

        combatant_attr = split_string[0]
        actions = split_string[1].split("|")
        effects = split_string[2]

        combatant = Combatant(
            name=combatant_attr[0],
            hp=combatant_attr[1],
            ac=combatant_attr[2],
            proficiency=combatant_attr[3],
            saves={"STR": combatant_attr[4],
                   "DEX": combatant_attr[5],
                   "CON": combatant_attr[6],
                   "WIS": combatant_attr[7],
                   "INT": combatant_attr[8],
                   "CHA": combatant_attr[9]},
            actions=[self.action_manager.load_action_from_serialized_name(a)
                     for a in actions]
        )

        return combatant
