/**
 * Created by Andrew on 1/16/18.
 */
import {setterAction} from './common'
import SimulatorSource from './sources/simulatorSource'


/* Action types */
export const SET_TEAM1_COMBATANTS = 'SET_TEAM1_COMBATANTS'
export const SET_TEAM2_COMBATANTS = 'SET_TEAM2_COMBATANTS'
export const INCREMENT_COUNTER = 'INCREMENT_COUNTER'
export const SET_ALL_COMBATANTS = 'SET_ALL_COMBATANTS'

export const setAllCombatants = setterAction(SET_ALL_COMBATANTS)
export const setT1Combatants = setterAction(SET_TEAM1_COMBATANTS)
export const setT2Combatants = setterAction(SET_TEAM2_COMBATANTS)
export const setCounter = setterAction(INCREMENT_COUNTER)


function updateCombatantSet(counter, oldSet, newSet) {
  // Get the new item by seeing what changed from the previous state (filter and get the first item)
  let newItem = newSet.filter(function(i) {return oldSet.indexOf(i) < 0;})[0];

  let updatedSet = newSet;

  // If there was a new item, then we add it to the current state by concatenating it
  // to the currentState value and append an arbitrary counter to the end to keep it unique.
  // If there isn't a new item in the state, then it was a delete and we simply take the newState
  if (newItem !== undefined) {
    updatedSet = oldSet.concat(
      {
        label: newItem.label,
        value: newItem.value + "_" + counter.toString()
      }
    )
  }

  return updatedSet
}

function addCombatantToSet(combatant, counter, set) {

  let updatedSet = set.concat({
    value: combatant.value + "_" + counter.toString(),
    label: combatant.label
  });

  return updatedSet
}

const get = (sourceFunc, action, key) => (...args) => (dispatch) => {
  sourceFunc(...args).then((res) => {
    let data = key ? res.data[key] : res.data
    dispatch(action(data))
  })
}

export const getAllCombatants = get(SimulatorSource.getCombatants, setAllCombatants)

export const updateT1Combatants = (newSet) => (dispatch, getState) => {
  let {team1Combatants, counter} = getState();
  // Must increment the counter each time to keep the appended values unique
  dispatch(setCounter(counter + 1));

  let updatedSet = updateCombatantSet(counter, team1Combatants, newSet);

  dispatch(setT1Combatants(updatedSet))
};

export const updateT2Combatants = (newSet) => (dispatch, getState) => {
  let {team2Combatants, counter} = getState();
  // Must increment the counter each time to keep the appended values unique
  dispatch(setCounter(counter + 1));

  let updatedSet = updateCombatantSet(counter, team2Combatants, newSet);

  dispatch(setT2Combatants(updatedSet))
};

export const addT1Combatant = (newCombatant) => (dispatch, getState) => {
  let {team1Combatants, counter} = getState();
  // Must increment the counter each time to keep the appended values unique
  dispatch(setCounter(counter + 1));

  dispatch(setT1Combatants(addCombatantToSet(newCombatant, counter, team1Combatants)))
};

export const addT2Combatant = (newCombatant) => (dispatch, getState) => {
  let {team2Combatants, counter} = getState();
  // Must increment the counter each time to keep the appended values unique
  dispatch(setCounter(counter + 1));

  dispatch(setT2Combatants(addCombatantToSet(newCombatant, counter, team2Combatants)))
};

