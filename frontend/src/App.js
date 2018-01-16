import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import CombatantColumn from './components/combatantColumn'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <div className="container">
          <div className="row-fluid">
            <div className="col-sm col-md col-lg">
              <p>BLAH BLAH</p>
            </div>
            <div className="col-sm col-md col-lg">
              <p>BLAH BLAH</p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
