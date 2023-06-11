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

def table_session_counter():
    # st.sesson counter intialization
    if 'table_session_counter' not in st.session_state:
        st.session_state.table_session_counter = 1
    st.session_state.table_session_counter = 1
    return st.session_state.table_session_counter

def table_delete_counter():
    # st.sesson counter intialization
    if 'table_delete_counter' not in st.session_state:
        st.session_state.table_delete_counter = 1
    st.session_state.table_delete_counter = 1
    return st.session_state.table_delete_counter

def column_session_counter():
    # st.sesson counter intialization
    if 'column_session_counter' not in st.session_state:
        st.session_state.column_session_counter = 1
    st.session_state.column_session_counter = 1
    return st.session_state.column_session_counter

def column_delete_counter():
    # st.sesson counter intialization
    if 'column_delete_counter' not in st.session_state:
        st.session_state.column_delete_counter = 1
    st.session_state.column_delete_counter = 1
    return st.session_state.column_delete_counter

def download_tables_counter():
    # st.sesson counter intialization
    if 'download_tables_counter' not in st.session_state:
        st.session_state.download_tables_counter = 1
    st.session_state.download_tables_counter = 1
    return st.session_state.download_tables_counter

def data_description_counter():
    # st.sesson counter intialization
    if 'data_description_counter' not in st.session_state:
        st.session_state.data_description_counter = 1
    st.session_state.data_description_counter = 1
    return st.session_state.data_description_counter

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

tab1, tab2, tab3 = st.tabs(['Describe data', 'Add table', 'Add column'])

with tab1:
    with st.form(key='descibe_data', clear_on_submit=False):
        st.markdown("### Describe your project")
        st.markdown("Here you can define the project in few sentences if you want.")
        col1, col2 = st.columns([2, 4])
        with col1:
            project_name = st.text_input("Enter database name", key='project_name')
        with col2:
            project_description = st.text_area("Describe your data", key='project_description')
        add_data_description = st.form_submit_button("Add project description", on_click=data_description_counter)

with tab2:
    with st.form(key='add_table', clear_on_submit=False):
        st.markdown("### Add table")
        st.markdown("Here we can define a new table and write a description about it.")
        col1, col2 = st.columns([2, 4])
        with col1:
            table_name = st.text_input("Enter table name", key='table_name')
        with col2:
            table_description = st.text_area("Enter table description", key='table_description')
        add_table = st.form_submit_button("Add Table", on_click=table_session_counter)

with tab3:
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
                column_description = st.text_area("Enter column description", key='column_description')
            with col3:
                column_type = st.selectbox("Select column type", ['Select', 'int', 'float', 'string', 'date', 'datetime'], key='column_type')
        add_column = st.form_submit_button("Add column", on_click=column_session_counter)


if 'table_session_counter' not in st.session_state:
    st.session_state.table_session_counter = 0
if 'column_session_counter' not in st.session_state:
    st.session_state.column_session_counter = 0
if 'table_delete_counter' not in st.session_state:
    st.session_state.table_delete_counter = 0
if 'column_delete_counter' not in st.session_state:
    st.session_state.column_delete_counter = 0

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
    if table_name == "":
        st.error("Table name cannot be empty")
    elif table_name in table_table['table_name'].unique():
        st.error("Table name already exists")
    else:
        table_table = pd.concat([table_table, pd.DataFrame({'table_name': [table_name], 'table_description': [table_description]})], ignore_index=True)
        st.session_state['table_table'] = table_table
        # refresh the page to see the changes
        st.experimental_rerun()

if st.session_state.column_session_counter == 1:
    st.session_state.column_session_counter = 0
    if column_name == "":
        st.warning("Column name cannot be empty")
    # elif if column exist already in the table, for this we alo need to check the table name
    elif column_table[(column_table['table_name'] == select_table) & (column_table['column_name'] == column_name)].shape[0] > 0:
        st.warning("Column not added because column name already exists in selected table")
    else:
        column_table = column_table.concat([column_table, pd.DataFrame({'table_name': [select_table], 'column_name': [column_name], 'column_description': [column_description], 'column_type': [column_type]})], ignore_index=True)
        st.session_state['column_table'] = column_table
        # refresh the page to see the changes
        st.experimental_rerun()

st.markdown("### Tables that we have defined")
col1, col2 = st.columns([4, 2])
with col1:
    st.write(table_table)
with col2:
    with st.form(key='delete_table', clear_on_submit=True):
        st.markdown("### Delete table")
        st.markdown("Here we can delete a table that we have defined before.")
        select_table = st.selectbox("Select table", table_table['table_name'].unique(), key='select_table_delete')
        delete_table = st.form_submit_button("Delete table", on_click=table_delete_counter)

st.markdown("### Columns that we have defined")
col1, col2 = st.columns([4, 2])
with col1:
    st.write(column_table)
with col2:
    column_unique_values = column_table['table_name'] + ' --- ' + column_table['column_name']
    with st.form(key='delete_column', clear_on_submit=True):
        st.markdown("### Delete column")
        st.markdown("Here we can delete a column that we have defined before.")
        # concat table_name and column_name to get unique values
        select_column = st.selectbox("Select column", column_unique_values, key='select_column_delete')
        delete_column = st.form_submit_button("Delete column", on_click=column_delete_counter)

if st.session_state.table_delete_counter == 1:
    st.session_state.table_delete_counter = 0
    table_table = table_table[table_table['table_name'] != select_table]
    st.session_state['table_table'] = table_table
    # refresh the page to see the changes
    st.experimental_rerun()

if st.session_state.column_delete_counter == 1:
    st.session_state.column_delete_counter = 0
    # split the unique value to get the table_name and column_name
    table_name, column_name = select_column.split(' --- ')
    # drop the row from the column_table where both of the values are the same as the selected values
    column_table = column_table[(column_table['table_name'] != table_name) | (column_table['column_name'] != column_name)]
    st.session_state['column_table'] = column_table
    # refresh the page to see the changes
    st.experimental_rerun()

st.markdown("***")

st.markdown("### Save the tables")
st.markdown("Here we can save the tables that we have defined as a pickle file.")
st.markdown("We can use the file to load the tables in the future.")

# create a dictionary with the table_table and the column_table and save it as a pickle file
combined_table = {'table_table': table_table, 'column_table': column_table}
datetime = pd.Timestamp.now().strftime("%Y-%m-%d_%H-%M-%S")

col1, col2 = st.columns([2, 1])

with col1:
    custom_filename = st.text_input("Enter custom filename if you want", key='file_name')
    if custom_filename != '':
        filename_to_use = f'{custom_filename}.pkl'
    else:
        filename_to_use = f'da_tool_export_{datetime}.pkl'
with col2:
    download_tables = st.download_button(label="Download tables",
                                        data=pickle.dumps(combined_table),
                                        file_name=filename_to_use,
                                        on_click=download_tables_counter)
