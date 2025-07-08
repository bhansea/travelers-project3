import React, { useState } from 'react';

function Form() {
    const [homeworld, setHomeworld] = useState('');
    const [unitType, setUnitType] = useState('');
    const [prediction, setPrediction] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        console.log(homeworld, unitType);
    };

    return (
        <div className="container">
            <form onSubmit={handleSubmit} className="mt-5">
                <div className="form-group">
                    <label htmlFor="homeworld">Homeworld </label>
                    <input
                        type="text"
                        className="form-control"
                        id="homeworld"
                        placeholder="Enter homeworld"
                        value={homeworld}
                        onChange={(e) => setHomeworld(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="unitType">Unit Type </label>
                    <input
                        type="unitType"
                        className="form-control"
                        id="unitType"
                        placeholder="Enter unit type"
                        value={unitType}
                        onChange={(e) => setUnitType(e.target.value)}
                    />
                </div>
                <button type="submit" className="btn btn-primary" style={{marginTop:20}}>Submit</button>
            </form>
        </div>
    );
}

export default Form;