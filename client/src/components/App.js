import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Form from './Form';
import Result from './Result';

const Banner = () => (
  <div className="banner">
    <h1 className="center-text">Titanic Game</h1>
    <p className="center-text">
        The Titanic tragically sunk in 1912. Despite its (very) short lived trip, the Titanic was a marvel of technology for its time.
        <br />
        Have you ever wondered if you would have survived, if you were on the ship? Wonder no more!
    </p>
  </div>
)

const Body = () => (
  <Switch>
    <Route exact path='/' component={Form} />
    <Route exact path='/result' component={Result} />
  </Switch>
)

const App = () => {
  return (
    <div className="App">
      <div className="App-container">
        <Banner />
        <Body />
      </div>
    </div>
  );
}

export default App;
