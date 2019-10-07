import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import axios from 'axios';

export const getResults = async (userObj) => {
    const header = { header: { 'Content-Type': 'application/json' }}
    const body = JSON.stringify(userObj);
    try {
        let res = await axios.post('/titanic', body, header, { withCredentials: false });
        return res;
    } catch(err) {
        console.error(err.message);
    }
}

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

const Form = () => {

    const [defaultState, changeState] = useState({
        sex: "Male",
        age: "",
        fare: "",
        family: "",
    });

    const handleChange = event => changeState({
        ...defaultState,
        [event.target.id]: event.target.value
    });

    const handleSubmit = event => {
        event.preventDefault();
        console.log(defaultState);
        const res = getResults(defaultState);
        return <Redirect to='/result' result={res} />
    }

    return (
        <form onSubmit={event => handleSubmit(event)}>
            <div className="form-group">
                <label htmlFor="sex">You are: </label>
                <select className="form-control" id="sex" value={defaultState.sex} onChange={event=>handleChange(event)}>
                    <option defaultValue>Male</option>
                    <option>Female</option>
                </select>
            </div>
            <div className="form-group">
                <label htmlFor="age">Your age: </label>
                <input className="form-control" type="number" id="age" aria-describedby="age" value={defaultState.age} onChange={event=>handleChange(event)} />
                <small id="age" className="form-text text-muted">We won't share this with anybody!</small>
            </div>
            <div className="form-group">
                <label htmlFor="fare">How much do you spend on tickets? </label>
                <input className="form-control" type="number" id="fare" aria-describedby="fare" value={defaultState.fare} onChange={event=>handleChange(event)} />
            </div>
            <div className="form-group">
                <label htmlFor="family">How many family members would you bring on a trip? </label>
                <input className="form-control" type="number" id="family" aria-describedby="family" value={defaultState.family} onChange={event=>handleChange(event)} />
            </div>
            <button type="submit" className="btn btn-block btn-primary">Find Out if you Survive!</button>
        </form>
    )
}



const Home = () => {
    return (
        <div className="App">
            <Banner />
            <Form />
        </div>
    )
}

export default Home;