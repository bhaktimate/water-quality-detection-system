import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Water Map", layout="wide")

st.title("🌍 Maharashtra Water Quality Map")

# ---------------- CITY COORDINATES ----------------
city_coords = {
    "Pune": [18.5204, 73.8567],
    "Mumbai": [19.0760, 72.8777],
    "Nagpur": [21.1458, 79.0882],
    "Nashik": [19.9975, 73.7898],
    "Aurangabad": [19.8762, 75.3433],
    "Solapur": [17.6599, 75.9064]
}

# ---------------- LOAD DATA ----------------
try:
    df = pd.read_csv("data/history.csv")
except:
    st.warning("⚠️ No data found. Run analysis first.")
    st.stop()

# ---------------- CREATE MAP ----------------
m = folium.Map(location=[19.5, 75.5], zoom_start=6)

# ---------------- ADD MARKERS ----------------
for _, row in df.iterrows():

    city = row["City"]
    prob = row["Probability"]
    result = row["Result"]

    coords = city_coords.get(city)

    if coords:

        if result == "SAFE":
            color = "green"
        elif result == "MODERATE":
            color = "orange"
        else:
            color = "red"

        folium.CircleMarker(
            location=coords,
            radius=10,
            color=color,
            fill=True,
            fill_color=color,
            popup=f"""
            <b>{city}</b><br>
            Result: {result}<br>
            Score: {round(prob,2)}
            """
        ).add_to(m)

# ---------------- DISPLAY ----------------
st_folium(m, width=900, height=500)
