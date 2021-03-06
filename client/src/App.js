import React, { useState } from 'react';
import axios from 'axios';

export const getResults = async (userObj) => {
    const config = { 
        header: { 
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    try {
        let res = await axios.post('/titanic', userObj, config);
        return res.data;
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

const App = () => {

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
        if (!defaultState.age || !defaultState.fare || !defaultState.family) {
            alert("Please fill out all the forms!");
        } else {

            var jsonForm = {
                sex: defaultState.sex,
                age: defaultState.age,
                fare: defaultState.fare,
                family: defaultState.family
            }

            getResults(jsonForm).then(res => {
                alert(res);
                window.location.reload();
            });
        }
    }

    return (
        <div className="App">
            <Banner />
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
        </div>
    )
}

export default App;