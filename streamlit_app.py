import streamlit as st
number = st.slider("Pick a number", 0, 100)

st.write("You're scheduled for:", number)
