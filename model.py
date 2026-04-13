import joblib
import numpy as np

# ---------------- LOAD MODEL ----------------
model = joblib.load("water_model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------- PREDICTION FUNCTION ----------------
def predict_water_quality(inputs):
    data = np.array([inputs])
    scaled = scaler.transform(data)

    # Get prediction & probabilities
    pred = model.predict(scaled)[0]
    probs = model.predict_proba(scaled)[0]

    # ---------------- AUTO DETECT CLASS INDEX ----------------
    classes = model.classes_

    # Find index of "1" (potable/safe)
    safe_index = list(classes).index(1)

    prob = probs[safe_index]

    # ---------------- SMART THRESHOLD ----------------
    if prob >= 0.65:
        result = "SAFE"
    elif prob >= 0.4:
        result = "MODERATE"
    else:
        result = "CONTAMINATED"

    # ---------------- RULE-BASED BOOST (VERY IMPORTANT) ----------------
    ph = inputs[0]
    turbidity = inputs[-1]

    if 6.5 <= ph <= 8.5 and turbidity < 5:
        if result == "CONTAMINATED":
            result = "MODERATE"
        elif result == "MODERATE":
            result = "SAFE"

    return prob, result