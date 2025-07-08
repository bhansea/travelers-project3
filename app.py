from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open("trained_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/api/predict", methods=["POST"])
def predict():
    print("Request Recevied")
    data = request.json
    homeworld = data.get("homeworld", "")
    unit_type = data.get("unit_type", "")

    df = pd.DataFrame([{
        "homeworld": homeworld,
        "unit_type": unit_type
    }])

    encoded = pd.get_dummies(df)
    encoded = encoded.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(encoded)[0]
    return jsonify({"prediction": "resistance" if prediction else "empire"})

if __name__ == "__main__":
    app.run(port=5001, debug=True)