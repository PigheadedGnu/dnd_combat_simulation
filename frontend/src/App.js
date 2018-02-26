import React, { Component } from 'react';
import {Route} from 'react-router'
import {BrowserRouter} from 'react-router-dom'
import CombatantScreen from './components/combatantScreen'
import ResultsScreen from './components/ResultsScreen'
import CombatantCreation from './components/combatantCreation'
import Header from './components/header'
import InfoScreen from './components/info'
import { connect } from 'react-redux'

const Homepage = ({...props}) => (
    <div>
        <Header{...props}/>
    </div>
);

const SimulatorScreen = ({...props}) => (
  <div>
    <CombatantScreen {...props}/>
    <ResultsScreen {...props}/>
  </div>
);

const Info = ({...props}) => (
    <div>
        <InfoScreen {...props}/>
    </div>
);

const mapStateToProps = (state) => ({

})

const mapDispatchToProps = (dispatch) => ({

})

const AppRouter = () => (
  <BrowserRouter>
    <div className="App">
      <Route path='/info/' component={Info}/>
      <Route path='/simulator/' component={SimulatorScreen}/>
      <Route path='/creation/' component={CombatantCreation}/>
      <Route exact path='/' component={Homepage}/>
    </div>
  </BrowserRouter>
)

export default connect(mapStateToProps, mapDispatchToProps)(AppRouter)

