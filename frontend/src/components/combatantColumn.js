/**
 * Created by Andrew on 1/15/18.
 */

import React, { Component } from 'react';
import '../App.css';
import ReactTable from "react-table";
import "react-table/react-table.css";

class CombatantColumn extends React.Component {
  constructor() {
    super();
    this.state = {
      data: [
        {
          "name": "Test1",
          "cr": 100,
          "creatureType": "Fire",
          "expDamage": 10000,
        },
        {
          "name": "Test2",
          "cr": 2,
          "creatureType": "Lightning",
          "expDamage": 1000,
        },]
    };
  }
  render() {
    const { data } = this.state;
    return (
      <div>
        <ReactTable
          data={data}
          columns={[
            {
              Header: "Name",
              columns: [
                {
                  Header: "Creature Name",
                  accessor: "name"
                },
              ]
            },
            {
              Header: 'Stats',
              columns: [
                {
                  Header: "Creature Rating",
                  accessor: "cr"
                },
                {
                  Header: "Type",
                  accessor: "creatureType"
                },
                {
                  Header: "Expected Damage",
                  accessor: "expDamage"
                },

              ]
            }
          ]}
          defaultPageSize={20}
          className="-striped -highlight"
        />
        <br />
      </div>
    );
  }
}

export default CombatantColumn;