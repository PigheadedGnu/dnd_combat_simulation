import React, { Component } from 'react';
import Select from 'react-select';
import 'react-select/dist/react-select.css';
import { connect } from 'react-redux'
import "react-table/react-table.css";
import * as actions from '../actions'
import Grid from 'react-css-grid';
import ActionTable from './actionTable'
import '../index.css';

const CombatantCreation = ({allActions, combatantActions, updateCombatantActions, addCombatantAction}) => (
  <div>
    <h1> Create a combatant:</h1>
    <Grid width={320} gap={32}>
      <div className="section">
        <input className="text-input" placeholder="Combatant name"/>
        <input className="text-input" placeholder="Hit points"/>
        <input className="text-input" placeholder="Armor class"/>
        <input className="text-input" placeholder="Proficiency bonus"/>
        <h3>Saves</h3>
        <Grid width={160} gap={20}>
          <div className="section">
            <input className="text-input" placeholder="Strength"/>
            <input className="text-input" placeholder="Dexterity"/>
            <input className="text-input" placeholder="Intelligence"/>
          </div>
          <div className="section">
            <input className="text-input" placeholder="Constitution"/>
            <input className="text-input" placeholder="Wisdom"/>
            <input className="text-input" placeholder="Charisma"/>
          </div>
        </Grid>
      </div>
      <div className="section">
        <Select
          closeOnSelect={false}
          multi={true}
          onChange={updateCombatantActions}
          options={allActions}
          placeholder="Add your combatant actions"
          removeSelected={true}
          value={combatantActions}
        />
        <ActionTable actionAddFunction={addCombatantAction}/>
      </div>
    </Grid>
    <button className="button" onClick={addCombatantAction} type="button">Create Combatant</button>
  </div>
)

class Container extends React.Component{
  constructor(props) {
    super(props)
    props.getAllActions()
  }

  render() {
    return <CombatantCreation {...this.props} />
  }
}

const mapStateToProps = (state) => ({
  allActions: state.combatantCreationReducer.allActions,
  combatantActions: state.combatantCreationReducer.combatantActions
})

const mapDispatchToProps = (dispatch) => ({
  getAllActions: () => dispatch(actions.getAllActions()),
  addCombatantAction: (combatantAction) => dispatch(actions.addCombatantAction(combatantAction)),
  updateCombatantActions: (updatedSet) => dispatch(actions.updateCombatantActions(updatedSet))
})

export default connect(mapStateToProps, mapDispatchToProps)(Container)