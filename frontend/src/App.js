import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import CombatantColumn from './components/combatantColumn'
import { Row, Col, Container } from 'react-grid-system';


class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <Container>
          <Row>
            <Col>
              <CombatantColumn/>
            </Col>
            <Col>
              <CombatantColumn/>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default App;
