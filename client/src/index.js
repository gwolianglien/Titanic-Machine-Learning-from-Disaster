import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import './index.css';
import './App.css';

import Home from './Home';
import Result from './Result';

const Router = () => (
    <Switch>
        <Route exact path='/' component={Home} />
        <Route exact path='/result' component={Result} />
    </Switch>
)

ReactDOM.render(
    <BrowserRouter>
        <Router />
    </BrowserRouter>
    , document.getElementById('root')
);