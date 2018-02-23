import React, { Component } from 'react';
import {Route} from 'react-router'
import {BrowserRouter} from 'react-router-dom'
import CombatantScreen from './components/combatantScreen'
import ResultsScreen from './components/ResultsScreen'
import CombatantCreation from './components/combatantCreation'
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

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Route path='/test/' render={<div/>}/>
      <Route path='/simulator/' component={CombatantScreen}/>
      <Route path='/creation/' component={CombatantCreation}/>
    </div>
  </BrowserRouter>
)

export default connect(mapStateToProps, mapDispatchToProps)(App)

