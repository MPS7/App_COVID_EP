import streamlit as st
number = st.slider("Pick a number", 0, 100)

st.write("You're scheduled for:", number)


st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
