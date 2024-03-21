import streamlit as st
import numpy as np
import pandas as pd
import time


st.header("COVID-19 Impact in El Paso County, TX")

st.divider()

col1, col2 = st.columns(2)

with col1:
    variant = st.radio(
    "Select variant features 👉",
    key="variant",
    options=["Escapes immunity easily", "Transmit faster and escapes immunity"],
    )

with col2:
    vacc = st.radio(
    "Select booster vaccination 👉",
    key="vacc",
    options=["No vaccination", "Equal booster vaccination campaign", "Equitable booster vaccination campaign"],
    )



print(variant)

st.divider()


st.button("Reset", type="primary")
if st.button('Run'):
    with st.spinner('Please wait...'):
    	time.sleep(10)
    	st.success('Done!')

    if (variant == "Escapes immunity easily"):
        if (vacc == "No vaccination"):
            sc = "A"

        if (vacc == "Equal booster vaccination campaign"):
            sc = "B"

        if (vacc == "Equitable booster vaccination campaign"):
            sc = "D"

    if (variant == "Transmit faster and escapes immunity"):
        if (vacc == "No vaccination"):
            sc = "E"

        if (vacc == "Equal booster vaccination campaign"):
            sc = "F"

        if (vacc == "Equitable booster vaccination campaign"):
            sc = "H"
	
    if (sc == "A"):
        hosp = 10612
        ratio = 88
        st.write('The variant will cause', hosp, ' hospitalizations, with ', ratio, '% of them Hispanics')

        st.image("Hosp_A.png")
        st.image("disp_A.png")

    if (sc == "B"):
        hosp = 4712
        ratio = 89
        st.write('The variant will cause', hosp, ' hospitalizations, with ', ratio, '% of them Hispanics')

        st.image("Hosp_B.png")
        st.image("disp_B.png")

    if (sc == "D"):
        hosp = 4590
        ratio = 81
        st.write('The variant will cause', hosp, ' hospitalizations, with ', ratio, '% of them Hispanics')

        st.image("Hosp_D.png")
        st.image("disp_D.png")

    if (sc == "E"):
        hosp = 10960
        ratio = 89
        st.write('The variant will cause', hosp, ' hospitalizations, with ', ratio, '% of them Hispanics')

        st.image("Hosp_E.png")
        st.image("disp_E.png")
   
    if (sc == "F"):
        hosp = 4627
        ratio = 89
        st.write('The variant will cause', hosp, ' hospitalizations, with ', ratio, '% of them Hispanics')

        st.image("Hosp_F.png")
        st.image("disp_F.png")

    if (sc == "H"):
        hosp = 4554
        ratio = 81
        st.write('The variant will cause', hosp, ' hospitalizations, with ', ratio, '% of them Hispanics')

        st.image("Hosp_H.png")
        st.image("disp_H.png")

else:
    st.write('No analysis is currently run')


st.divider()
col1, col2 = st.columns(2)

with col1:	
    st.write("By: Dr. Anass Bouchnita")
    st.write("Department of Mathematical Sciences")
    st.write("contact: abouchnita@utep.edu")


with col2:
    st.image("utep.jpg", width = 150)

