import { combineReducers } from 'redux'
import * as t from '../actions'
import {setterReducer} from '../common'

const allActions = setterReducer([], t.SET_ALL_ACTIONS)
const combatantActions = setterReducer([], t.SET_COMBATANT_ACTIONS)

const reducer = combineReducers({
  allActions,
  combatantActions
})

export {reducer as default}