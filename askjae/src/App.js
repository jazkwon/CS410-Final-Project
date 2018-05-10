import React, { Component } from 'react';
import { Button, Grid, Image, Search, Dropdown, Menu, Checkbox, Form } from 'semantic-ui-react'
import logo from './logo.svg';
import './App.css';
import _ from 'lodash'


class App extends Component {
  constructor() {
      super();
      this.state = {
          searchText: '',
          searchResults: []
      }
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={require('./jaelogo.png')} className="App-logo" alt="logo" />
            <Form size='big'>
              <Form.Field className="searchbar" width='fourteen' >
                <input className="input"
                  placeholder='...Type Here' />
              </Form.Field>
              <Button type='submit'>Submit</Button>
            </Form>
        </header>
      </div>
    );
  }
}

export default App;
