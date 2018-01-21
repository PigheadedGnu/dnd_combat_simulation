import React, { Component } from 'react';
import './App.css';
import CombatantScreen from './components/combatantScreen'
import { connect } from 'react-redux'

const App = ({...props}) => (
  <div className="App">
    <header className="App-header">
      <h1 className="App-title">Welcome to DnD 5e Combat Simulator</h1>
    </header>
    <CombatantScreen {...props}/>
  </div>
);

const mapStateToProps = (state) => ({

})

const mapDispatchToProps = (dispatch) => ({

})

export default connect(mapStateToProps, mapDispatchToProps)(App)

