import streamlit as st
import pandas as pd
import numpy as np
from utils.da_functions import *
from PIL import Image
import pickle

st.set_page_config(layout='wide', page_title='Data Analysis Dashboard')
st.title("Load Data")

if 'table_table' not in st.session_state:
    table_table = pd.DataFrame(columns=['table_name', 'table_description'])
    st.session_state['table_table'] = table_table
else:
    table_table = st.session_state.table_table

if 'column_table' not in st.session_state:
    column_table = pd.DataFrame(columns=['table_name', 'column_name', 'column_description', 'column_type'])
    st.session_state['column_table'] = column_table
else:
    column_table = st.session_state.column_table


st.markdown("### Load the tables from saved file")
st.markdown("Here you can load the tables that you saved before by selecting the pickle file that you saved on the 'Define data' page.")
st.markdown("Once the tables are loaded, you can look at it and delete/ modify tables and columns on the 'Define data' page.")

uploaded_file = st.file_uploader("Upload File that you saved before")
if uploaded_file is not None:
    uploaded_dict = pickle.load(uploaded_file)
    uploaded_table_table = uploaded_dict['table_table']
    uploaded_column_table = uploaded_dict['column_table']
    st.write(uploaded_table_table)
    st.write(uploaded_column_table)
    st.session_state['table_table'] = uploaded_table_table
    st.session_state['column_table'] = uploaded_column_table
