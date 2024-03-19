import streamlit as st

st.write("COVID-19 Impact in El Paso County, TX")

high = st.radio(
    "Select variant features 👉",
    key="visibility",
    options=["Highly transmissible", "Immune escaping", "Both"],
)
