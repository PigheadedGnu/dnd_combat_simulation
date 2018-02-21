from random import randint
from core.settings import BASE_DIR
import json


def calc_roll(dice):
    """
    :param dice: A dictionary of (faces, amount) pairs
    """
    total = 0
    for max_roll, num_dice in dice.items():
        total += sum(map(lambda x: randint(1, max_roll), range(num_dice)))
    return total


def d20():
    # Roll a d20
    return randint(1, 20)


def load_dice(dice):
    """ Load a dictionary of dice from json into a usable dice object.

        When the dice are read from a JSON file, the key is a string, so must
         be turned into an integer here.
    """
    return {int(k): v for k, v in dice.items()}


def write_json_to_file(f_name, obj_to_write):
    with open(BASE_DIR + '/data/' + f_name, 'r') as f:
        current_info = json.load(f)
        if obj_to_write['name'] in current_info:
            # TODO: Return a message here and pass it forward for an API
            pass
    with open(BASE_DIR + '/data/' + f_name, 'w') as f:
        current_info[obj_to_write['name']] = obj_to_write
        json.dump(current_info, f, indent=2)


def capitalize(lower_string):
    split_string = lower_string.split(" ")
    ret_split_str = []
    for substr in split_string:
        capital_first = substr[0].upper()
        ret_split_str.append(capital_first + substr[1:])
    return " ".join(ret_split_str)