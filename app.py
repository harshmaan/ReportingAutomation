import streamlit as streamlit

import numpy as np 
import pandas as pd
import joblib 

model = joblib.load('xgbpipe.joblib')

st.title('Business Intelligence SQL Migration Automation Tool :report:')
st.text_input('Enter sql file name', "Please enter your file name in format: FILE_NAME_DATE")
st.select_slider('Choose base sql class',['Teradata','Oracle','DVT'])
st.select_slider('Choose target sql class',['Snowflake','Oracle'])
st.text_input('Enter sql file', "Please paste your base sql here")


def convert():
	st.success('Conversion successful :thumbsup:')

st.button('Convert', on_clock=convert)
