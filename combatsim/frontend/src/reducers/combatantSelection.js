/**
 * Created by Andrew on 1/17/18.
 */
import { combineReducers } from 'redux'
import * as t from '../actions'
import {setterReducer} from '../common'

const team1Combatants = setterReducer([], t.SET_TEAM1_COMBATANTS)
const team2Combatants = setterReducer([], t.SET_TEAM2_COMBATANTS)
const counter = setterReducer(0, t.INCREMENT_COUNTER)
const allCombatants = setterReducer(
  [
    {value: 'goblin', label: 'Goblin', cr: 0, creatureType: 'humanoid'},
    {value: 'orc', label: 'Orc', cr: 1, creatureType: 'humanoid'}
  ], t.SET_ALL_COMBATANTS)

const reducer = combineReducers({
  team1Combatants,
  team2Combatants,
  counter,
  allCombatants
})

export {reducer as default}