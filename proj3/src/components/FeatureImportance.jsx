import React, { useState } from 'react';

function FeatureImportance() {
    const [featureImportance, setFeatureImportance] = useState(false)
    
    function handleClick() {
        setFeatureImportance(!featureImportance)
    }

    return (
        <div>
            <button onClick={handleClick}>{featureImportance ? "Hide Feature Importance Chart" : "Show Feature Importance Chart"} </button>

            {featureImportance && (
                <div>
                    <img src='http://localhost:5001/api/feature_importance' alt='Feature Importance Chart'></img>
                </div>
            )}
        </div>
    );
}

export default FeatureImportance