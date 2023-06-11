import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.da_functions import *
from PIL import Image
import plotly.graph_objects as go
import plotly.io as pio

st.set_page_config(layout='wide', page_title='Data Analysis Dashboard')
st.title("Define Data")

def table_session_counter():
    # st.sesson counter intialization
    if 'table_session_counter' not in st.session_state:
        st.session_state.table_session_counter = 1
    st.session_state.table_session_counter = 1
    return st.session_state.table_session_counter

def column_session_counter():
    # st.sesson counter intialization
    if 'column_session_counter' not in st.session_state:
        st.session_state.column_session_counter = 1
    st.session_state.column_session_counter = 1
    return st.session_state.column_session_counter

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


with st.form(key='add_table', clear_on_submit=False):
    st.markdown("### Add table")
    st.markdown("Here we can define a new table and write a description about it.")
    col1, col2 = st.columns([2, 4])
    with col1:
        table_name = st.text_input("Enter table name", key='table_name')
    with col2:
        table_description = st.text_input("Enter table description", key='table_description')
    add_table = st.form_submit_button("Add Table", on_click=table_session_counter)

with st.form(key='add_column', clear_on_submit=True):
    st.markdown("### Add column to existing table")
    st.markdown("Here we can add a column to an existing table that we created before.")
    select_table = st.selectbox("Select table", table_table['table_name'].unique(), key='select_table')
    # if table_list is not empty
    if len(table_table) > 0:
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            column_name = st.text_input("Enter column name", key='column_name')
        with col2:
            column_description = st.text_input("Enter column description", key='column_description')
        with col3:
            column_type = st.selectbox("Select column type", ['int', 'float', 'string', 'date', 'datetime'], key='column_type')
    add_column = st.form_submit_button("Add column", on_click=column_session_counter)


if 'table_session_counter' not in st.session_state:
    st.session_state.table_session_counter = 0
if 'column_session_counter' not in st.session_state:
    st.session_state.column_session_counter = 0

if 'user_input_list' not in st.session_state:
    user_input_list = []
    st.session_state['user_input_list'] = user_input_list
else:
    user_input_list = st.session_state.user_input_list
if 'chatbot_response_list' not in st.session_state:
    chatbot_response_list = []
    st.session_state['chatbot_response_list'] = chatbot_response_list
else:
    chatbot_response_list = st.session_state.chatbot_response_list


if st.session_state.table_session_counter == 1:
    st.session_state.table_session_counter = 0
    st.write("Table button was clicked")
    table_table = table_table.append({'table_name': table_name, 'table_description': table_description}, ignore_index=True)
    st.session_state['table_table'] = table_table
    # refrresg the page
    st.experimental_rerun()

if st.session_state.column_session_counter == 1:
    st.session_state.column_session_counter = 0
    st.write("Column button was clicked")
    column_table = column_table.append({'table_name': select_table, 'column_name': column_name, 'column_description': column_description, 'column_type': column_type}, ignore_index=True)
    st.session_state['column_table'] = column_table
    # refrresg the page
    st.experimental_rerun()

st.markdown("### Tables that we have defined")
st.write(table_table)
st.markdown("### Columns that we have defined")
st.write(column_table)


