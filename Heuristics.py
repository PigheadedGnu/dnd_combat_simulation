import random
from settings import VERBOSITY


class Heuristic:
    name = ""


class TargetSelectionHeuristic(Heuristic):
    def __init__(self):
        pass

    def select(self, targets):
        if VERBOSITY > 2:
            print("Selecting random monster")
        return random.choice(targets)


class HighestHealth(TargetSelectionHeuristic):
    def __init__(self):
        super().__init__()
        pass

    def select(self, targets):
        if VERBOSITY > 2:
            print("Selecting monster with the highest health")
        return max(targets, key=lambda t: t.hp)


class LowestHealth(TargetSelectionHeuristic):
    def __init__(self):
        super().__init__()
        pass

    def select(self, targets):
        if VERBOSITY > 2:
            print("Selecting monster with the lowest health")
        return min(targets, key=lambda t: t.hp)
