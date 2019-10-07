import React from 'react';

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

const ResultContainer = (props) => (
    <div className="">
        {props.result}
    </div>
)

const Result = (props) => {
    return (
        <div className="App">
            <Banner />
            <ResultContainer result={props.result} />
        </div>
    )
}

export default Result