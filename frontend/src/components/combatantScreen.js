import React, { Component } from 'react';
import Select from 'react-select';
import 'react-select/dist/react-select.css';
import { connect } from 'react-redux'
import * as actions from '../actions'
import Grid from 'react-css-grid';
import CombatantTable from './combatantTable'
import '../index.css';

const CombatantScreen = ({team1Combatants, team2Combatants, allCombatants, team1Update, team2Update,
                         team1Add, team2Add, runSimulation, buttonText}) => (
  <div>
    <Grid width={320} gap={32}>
      <div className="section">
        <Select
          closeOnSelect={false}
          multi={true}
          onChange={team1Update}
          options={allCombatants}
          placeholder="Choose your combatants!"
          removeSelected={false}
          value={team1Combatants}
        />
        <CombatantTable teamAddFunction={team1Add}/>
      </div>
      <div className="section">
        <Select
          closeOnSelect={false}
          multi={true}
          onChange={team2Update}
          options={allCombatants}
          placeholder="Choose your combatants!"
          removeSelected={false}
          value={team2Combatants}
        />
        <CombatantTable teamAddFunction={team2Add}/>
      </div>
    </Grid>
    <button id="combatButton" className="button" onClick={runSimulation} type="button">{buttonText}</button>
  </div>
)

class Container extends React.Component{
  constructor(props) {
    super(props)
    props.getAllCombatants()
  }

  buttonDisabled() {
    return this.props.team1Combatants.length === 0 || this.props.team2Combatants.length === 0;
  }

  render() {
    let btn = document.getElementById("combatButton");
    let buttonText = "A Team is Empty!";
    if (btn) {
        btn.disabled = this.buttonDisabled();
        if (!this.buttonDisabled()){
          buttonText = "Fight!"
        }
    }
    return <div>
      <CombatantScreen {...this.props} buttonText={buttonText} />
    </div>
  }
}

const mapStateToProps = (state) => ({
  team1Combatants: state.combatantSelectionReducer.team1Combatants,
  allCombatants: state.combatantSelectionReducer.allCombatants,
  team2Combatants: state.combatantSelectionReducer.team2Combatants,
})

const mapDispatchToProps = (dispatch) => ({
  getAllCombatants: () => dispatch(actions.getAllCombatants()),
  team1Update: (newSet) => dispatch(actions.updateT1Combatants(newSet)),
  team2Update: (newSet) => dispatch(actions.updateT2Combatants(newSet)),
  team1Add: (newSet) => dispatch(actions.addT1Combatant(newSet)),
  team2Add: (newSet) => dispatch(actions.addT2Combatant(newSet)),
  runSimulation: () => dispatch(actions.runSimulation())
})

export default connect(mapStateToProps, mapDispatchToProps)(Container)