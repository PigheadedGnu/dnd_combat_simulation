import React, { Component } from 'react';
import { connect } from 'react-redux'
import '../index.css';

const InfoScreen = ({title}) => (
    <div>
        <p>Lorem ipsum placeholder text blah blah blah</p>
    </div>
)

class Container extends React.Component{
    constructor(props) {
        super(props)
    }

    render() {
        return <div>
            <InfoScreen {...this.props} title="Summary"/>
        </div>
    }
}

const mapStateToProps = (state) => ({
})

const mapDispatchToProps = (dispatch) => ({
})

export default connect(mapStateToProps, mapDispatchToProps)(Container)