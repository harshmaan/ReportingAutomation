import streamlit as st

import numpy as np 
import pandas as pd
from io import StringIO

__version__ = "1.0"
app_name = "SQL Migration Tool"

st.set_page_config(page_title="Reporting: SQL Migration Automation Tool", page_icon="📖", layout="wide")
st.header("Reporting: SQL Migration Automation Tool 📖")

if "count" not in st.session_state:
      st.session_state.count.count = 0

base_file_name = st.text_input('Enter sql file name', "")

uploaded_file = st.file_uploader("Choose your sql file")
if uploaded_file is not None:
    string_data = StringIO.read()
    st.write(string_data)


sql_class = ['Teradata','Oracle','Snowflake']

def ui_spacer(n=2, line=False, next_n=0):
	for _ in range(n):
		st.write('')
	if line:
		st.tabs([' '])
	for _ in range(next_n):
		st.write('')

def convert():
	st.success('Conversion successful :thumbsup:')
        


def ui_info():
    st.markdown(f"""
	SQL Migration Tool
	version {__version__}
	""")
    ui_spacer(1)
    st.markdown(f"""
    Please select below configuration. 
	""")

def sql_base_class_config():
    base_final = st.radio('Choose Base SQL Type', sql_class) 

def sql_target_class_config():
    target_final = st.radio('Choose Target SQL Type', sql_class)

def credits():
    ui_spacer(1)
    st.write("Made by [Harsh Maan](https://www.linkedin.com/in/harsh-maan-6b5727178/).", unsafe_allow_html=True)

def like_counter():
      st.session_state.count += 1

with st.sidebar:
    ui_info()
    ui_spacer(1)
    st.radio('Choose Base SQL Type', sql_class)
    st.radio('Choose Target SQL Type', sql_class)
    ui_spacer(2)
    credits()

st.button('Convert', on_click=convert)



st.button('Like', on_click=like_counter)

st.write('Total Portfolio likes: ', st.session_state.count)
