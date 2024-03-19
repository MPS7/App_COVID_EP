import streamlit as st

st.write("COVID-19 Impact in El Paso County, TX")

st.radio(
    "Select variant features 👉",
    key="visibility",
    options=["visible", "hidden", "collapsed"],
)
