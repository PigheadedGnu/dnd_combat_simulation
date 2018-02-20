/**
 * Created by Andrew on 1/17/18.
 */
import { combineReducers } from 'redux'
import * as t from '../actions'
import {setterReducer} from '../common'
import {SET_SIMULATION_RESULTS} from "../actions";

const team1Combatants = setterReducer([], t.SET_TEAM1_COMBATANTS)
const team2Combatants = setterReducer([], t.SET_TEAM2_COMBATANTS)
const counter = setterReducer(0, t.INCREMENT_COUNTER)
const allCombatants = setterReducer(
  [
    {value: 'goblin', label: 'Goblin', cr: 0, creatureType: 'humanoid'},
    {value: 'orc', label: 'Orc', cr: 1, creatureType: 'humanoid'}
  ], t.SET_ALL_COMBATANTS)
const simulationResults = setterReducer(
  {"avg_num_rounds": "-",
   "avg_t1_deaths": "-",
   "num_times_at_least_one_t1_death": "-",
   "perc_time_t1_won": "-",
   "avg_num_round_when_t1_won": "-",
   "avg_num_round_when_t2_won": "-"
  },
t.SET_SIMULATION_RESULTS);

const reducer = combineReducers({
  team1Combatants,
  team2Combatants,
  counter,
  allCombatants,
  simulationResults
})

export {reducer as default}