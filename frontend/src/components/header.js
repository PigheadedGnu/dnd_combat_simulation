import React, { Component } from 'react';
import { connect } from 'react-redux'
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import CombatantScreen from './combatantScreen'
import ResultsScreen from './ResultsScreen'
import CombatantCreation from './combatantCreation'
import InfoScreen from './info'


import '../index.css';

const Header = ({title}) => (
    <div>
        <h1>{title}</h1>
          <Tabs>
            <TabList>
              <Tab>General</Tab>
              <Tab>Simulator</Tab>
              <Tab>Character Creation</Tab>
            </TabList>
              <TabPanel>
                  <h2>Frequently Asked Questions and General Information</h2>
                  <InfoScreen {...this.props}/>
              </TabPanel>
              <TabPanel>
                  <h2>Simulate a DnD Battle</h2>
                  <CombatantScreen {...this.props}/>
                  <ResultsScreen {...this.props}/>
              </TabPanel>
              <TabPanel>
                  <h2>Create a Custom Character</h2>
                  <CombatantCreation {...this.props}/>
              </TabPanel>
          </Tabs>
    </div>
)

class Container extends React.Component{
    constructor(props) {
        super(props)
    }

    render() {
        return <div>
            <Header {...this.props} title="DnD Combat Simulator"/>
        </div>
    }
}

const mapStateToProps = (state) => ({
})

const mapDispatchToProps = (dispatch) => ({
})

export default connect(mapStateToProps, mapDispatchToProps)(Container)
