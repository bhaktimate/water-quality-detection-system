import streamlit as st
import pandas as pd
import plotly.express as px

# LOAD CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📊 Water Quality Dashboard")

try:
    df = pd.read_csv("data/history.csv")
except:
    st.warning("No data available yet.")
    st.stop()

st.subheader("📈 Trend Over Time")
fig1 = px.line(df, x="Time", y="Probability", color="City")
st.plotly_chart(fig1)

st.subheader("🏙️ City Comparison")
fig2 = px.bar(df, x="City", y="Probability", color="Result")
st.plotly_chart(fig2)

st.subheader("🧪 pH Distribution")
fig3 = px.histogram(df, x="pH")
st.plotly_chart(fig3)

st.dataframe(df)
