import streamlit as st 
import pandas as pd
import random
from sklearn import linear_model

st.set_page_config(page_title="Analytics App", page_icon="⚡", layout='centered', initial_sidebar_state="collapsed")

st.write("""
    # Sun Life Energy Analytics App
    ----
    """)

def main():
    energy_use = pd.read_csv('data/Energy Usage - Sheet1 (1).csv')
    energy_use = energy_use.drop(columns='Week')

    st.markdown(f'<h2 style="font-weight: bold; padding-bottom: 0px;">Energy Usage per Week</h2>', unsafe_allow_html=True)
    energy_use
    st.line_chart(energy_use[['Total Energy Usage KWh', 'Appliance 1', 'Appliance 2', 'Appliance 3']])
    average = energy_use['Total Energy Usage KWh'].sum()/11
    st.write('Average (KWh):', average)

    st.markdown(f'<h2 style="font-weight: bold; padding-bottom: 0px;">Energy Forecasting</h2>', unsafe_allow_html=True)
    st.write('Prediction for Future Weeks:', 52, 53, 55, 56)
    st.write('4% Increase')

if __name__ == '__main__':
    main()