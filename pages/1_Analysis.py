import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

from model import predict_water_quality
from utils import get_suggestions

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Water Analysis", layout="wide")

# ---------------- LOAD CSS ----------------
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🔬 Water Quality Analysis")
st.caption("AI-based smart water quality detection")

# ---------------- CITY ----------------
city = st.selectbox(
    "📍 Select City",
    ["Pune", "Mumbai", "Nagpur", "Nashik", "Aurangabad", "Solapur"]
)

# ---------------- INPUTS ----------------
st.subheader("🧪 Enter Water Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    ph = st.slider("pH", 0.0, 14.0, 7.0)
    hardness = st.slider("Hardness", 0.0, 300.0, 120.0)
    solids = st.slider("Solids", 0.0, 20000.0, 8000.0)

with col2:
    chloramines = st.slider("Chloramines", 0.0, 15.0, 6.5)
    sulfate = st.slider("Sulfate", 0.0, 500.0, 250.0)
    conductivity = st.slider("Conductivity", 0.0, 1000.0, 400.0)

with col3:
    organic_carbon = st.slider("Organic Carbon", 0.0, 30.0, 10.0)
    trihalomethanes = st.slider("Trihalomethanes", 0.0, 150.0, 70.0)
    turbidity = st.slider("Turbidity", 0.0, 10.0, 3.0)

# ---------------- ANALYZE ----------------
if st.button("🔍 Analyze Water"):

    inputs = [
        ph, hardness, solids, chloramines,
        sulfate, conductivity, organic_carbon,
        trihalomethanes, turbidity
    ]

    # Prediction
    prob, result = predict_water_quality(inputs)

    # ---------------- RESULT STYLE ----------------
    if result == "SAFE":
        css_class = "safe"
    elif result == "MODERATE":
        css_class = "moderate"
    else:
        css_class = "bad"

    # ---------------- RESULT CARD ----------------
    st.markdown(f"""
    <div class="card {css_class}">
        <h2 style="text-align:center;">{result}</h2>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- CONFIDENCE ----------------
    st.write(f"📊 Confidence Score: {round(prob,2)}")
    st.progress(float(prob))

    # ---------------- GAUGE ----------------
    st.subheader("📊 Water Quality Meter")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={'text': "Quality Score (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "blue"},
            'steps': [
                {'range': [0, 40], 'color': "red"},
                {'range': [40, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "green"}
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    # ---------------- SAVE DATA ----------------
    new_data = pd.DataFrame([{
        "Time": datetime.now(),
        "City": city,
        "pH": ph,
        "Result": result,
        "Probability": prob
    }])

    try:
        old = pd.read_csv("data/history.csv")
        df = pd.concat([old, new_data], ignore_index=True)
    except:
        df = new_data

    df.to_csv("data/history.csv", index=False)

    # ---------------- SUGGESTIONS ----------------
    st.subheader("💡 Suggestions")

    tips = get_suggestions(inputs)

    if tips:
        for t in tips:
            st.write("•", t)
    else:
        st.success("Water looks safe 👍")
