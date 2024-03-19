import streamlit as st
import numpy as np
import time


st.header("COVID-19 Impact in El Paso County, TX")


col1, col2, col3 = st.columns(3)

with col1:
    variant = st.radio(
    "Select variant features 👉",
    key="variant",
    options=["Highly transmissible", "Immune escaping", "Both"],
    )

with col2:
    vacc = st.radio(
    "Select booster vaccination coverage 👉",
    key="vacc",
    options=["30 %", "10 %", "0 %"],
    )

with col3:
    #st.write("UTEP Mathematical Sciences Department")
    st.image("utep.jpg")
    







print(variant)




st.button("Reset", type="primary")
if st.button('Run simulation'):
    with st.spinner('Wait for it...'):
    	time.sleep(5)
    	st.success('Done!')

    data = np.random.randn(10, 1)

    st.subheader("A wide column with a chart")
    st.line_chart(data)
else:
    st.write('Goodbye')
