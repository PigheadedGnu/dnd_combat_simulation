import os

import numpy as np

from data.players import *
from settings import *
from src.heuristics.target_selection_heuristics import *
from src.heuristics.heuristic_container import *

from src.simulator import Simulator

if os.path.exists("./DM_enemies.py"):
    from data.DM_enemies import *

pcs = [Marshall(), Freddy(), Johnny(), Max()]
enemies = [green_dragon()]
heuristics = HeuristicContainer(LowestHealthPercentage(), LowestHealthPercentageBelowThreshold())


number_of_rounds = []
number_of_player_deaths = []
winning_teams = []
for i in range(NUM_TRIALS):
    sim = Simulator(pcs, enemies)
    num_rounds, num_player_deaths, winning_team = sim.run_battle(heuristics)
    number_of_player_deaths.append(num_player_deaths)
    winning_teams.append(winning_team)
    number_of_rounds.append(num_rounds)

if NUM_TRIALS > 1:
    print("Average number of rounds:", np.mean(number_of_rounds))
    print("Average number of player deaths", np.mean(number_of_player_deaths))
    print("Number of times at least 1 player death:",
          len([x for x in number_of_player_deaths if x > 0]))
    print("Percent of times players won:", 1 - np.mean(winning_teams))

    players_won = [number_of_rounds[i] for i in range(NUM_TRIALS) if winning_teams[i] == 0]
    monsters_won = [number_of_rounds[i] for i in range(NUM_TRIALS) if winning_teams[i] == 1]
    if players_won:
        print("Average number of rounds when player won:", np.mean(players_won))
    if monsters_won:
        print("Average number of rounds when monsters won:", np.mean(monsters_won))