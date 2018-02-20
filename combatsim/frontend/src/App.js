import React, { Component } from 'react';
import './App.css';
import CombatantScreen from './components/combatantScreen'
import ResultsScreen from './components/ResultsScreen'
import { connect } from 'react-redux'

const App = ({...props}) => (
  <div className="App">
    <CombatantScreen {...props}/>
    <ResultsScreen {...props}/>
  </div>
);

const mapStateToProps = (state) => ({

})

const mapDispatchToProps = (dispatch) => ({

})

export default connect(mapStateToProps, mapDispatchToProps)(App)

