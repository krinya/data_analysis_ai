import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.da_functions import *
from PIL import Image
import plotly.graph_objects as go
import plotly.io as pio
import pickle

st.set_page_config(layout='wide', page_title='Data Analysis Dashboard')
st.title("Define Data")

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


st.markdown("### Load the tables from file")
st.markdown("Here you can load the tables that you saved before by selecting the pickle file that you saved.")
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
