import React, { Component } from 'react';
import Select from 'react-select';
import 'react-select/dist/react-select.css';
import { connect } from 'react-redux'
import * as actions from '../actions'


const CombatantSelect = ({combatants, allCombatants, updateFunc}) => {
  return (
    <div className="section">
      <Select
        closeOnSelect={false}
        multi={true}
        onChange={updateFunc}
        options={allCombatants}
        placeholder="Choose your combatants!"
        removeSelected={false}
        value={combatants}
      />
    </div>
  );
}

class Container extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return <CombatantSelect {...this.props} />
  }
}

const mapStateToProps = (state) => ({
  ...state.concernPerception,

})

export default CombatantSelect;