import streamlit as st
import pandas as pd
import numpy as np
from utils.da_functions import *
from PIL import Image
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

def programing_language_counter():
    # st.sesson counter intialization
    if 'programing_language_counter' not in st.session_state:
        st.session_state.programing_language_counter = 1
    st.session_state.programing_language_counter = 1
    return st.session_state.programing_language_counter

def table_csv_counter():
    # st.sesson counter intialization
    if 'table_csv_counter' not in st.session_state:
        st.session_state.table_csv_counter = 0
    st.session_state.table_csv_counter = 1
    return st.session_state.table_csv_counter

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

if 'table_csv_counter' not in st.session_state:
    st.session_state['table_csv_counter'] = 0

column_type_input_list = ['Select', 'int', 'binary', 'float', 'string', 'date', 'datetime']

#tab1, tab2, tab3, tab4 = st.tabs(['Using a CSV file', 'Add tables manualy', 'Add columns to existing tables manualy', 'Describe data'])
tab1, tab2, tab3 = st.tabs(['Using a CSV file', 'Add tables manualy', 'Add columns to existing tables manualy'])

with tab1:
    st.markdown("### Upload table as a CSV")
    st.markdown("Here you can upload your data as a CSV file to define your table name and column structure for the chatbot.")
    col1, col2 = st.columns([2, 2])
    with col1:
        uploaded_csv_file = st.file_uploader("Choose a CSV file", type="csv")
    with col2:
        show_imported_data_head = st.checkbox("Show imported data head", key='show_imported_data_head', value=False)
    if uploaded_csv_file is not None:
        imported_df = pd.read_csv(uploaded_csv_file)
        if show_imported_data_head:
            st.dataframe(imported_df.head(10))
        st.markdown("### Name your table")
        col1, col2 = st.columns([2, 4])
        with col1:
            table_name_csv = st.text_input("Enter table name")
        with col2:
            table_description_csv = st.text_area("Enter table description")
        st.markdown("### Add column to table")
        st.markdown("Here we list to all your columns ion the table to define them. You can select the columns you want to import and give some description about it and then select the column type.")
        col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
        # get all colnames from imported_df
        colnames = imported_df.columns
        # get all coltypes from imported_df
        coltypes = imported_df.dtypes
        # create a pandas table with colnames, coldescription and coltype
        column_table_csv = pd.DataFrame(columns=['table_name', 'column_name', 'column_description', 'column_type'])
        # in a for loop create a selectbox for each column
        col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
        with col1:
            st.markdown("#### Select columns to import")
        with col2:
            st.markdown("#### Describe columns")
        with col3:
            st.markdown("#### Select column type")
        for c in range(len(colnames)):
            col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
            with col1:
                add_colukmn_cb = st.checkbox(f"""**{colnames[c]}**""", key=f"""column_name_{c}""")
            with col2:
                column_description = st.text_area("Enter column description if you want to share more information about it",
                                                  key=f"""column_description_{c}""")
            with col3:
                column_type = st.selectbox("Select column type", column_type_input_list,
                                           key=f"""column_type_{c}""")
                st.write(f"""detected as a {coltypes[c]}, please select the correct type""")
            if add_colukmn_cb:
                column_table_csv = pd.concat([column_table_csv, pd.DataFrame({'table_name': [table_name_csv], 'column_name': [colnames[c]], 'column_description': [column_description], 'column_type': [column_type]})], ignore_index=True)
            if add_colukmn_cb == False:
                # delete the row from column_table_csv
                column_table_csv = column_table_csv[column_table_csv['column_name'] != colnames[c]]
            

        add_csv_table = st.button("Add table", on_click=table_csv_counter)
        if st.session_state.table_csv_counter == 1:
            with st.spinner("Adding table and columns to the tool..."):
                st.session_state.table_csv_counter = 0
                table_table = pd.concat([table_table, pd.DataFrame({'table_name': [table_name_csv], 'table_description': [table_description_csv]})], ignore_index=True)
                st.session_state['table_table'] = table_table
                column_table = pd.concat([column_table, column_table_csv], ignore_index=True)
                st.session_state['column_table'] = column_table
                # rerun the app
                st.experimental_rerun()    
with tab2:
    with st.form(key='add_table', clear_on_submit=False):
        st.markdown("### Add table")
        st.markdown("Here you can define a new table and write a description about it for the chatbot.")
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
                column_type = st.selectbox("Select column type", column_type_input_list, key='column_type')
        add_column = st.form_submit_button("Add column", on_click=column_session_counter)

# with tab4:
#     with st.form(key='descibe_data', clear_on_submit=False):
#         st.markdown("### Describe your project")
#         st.markdown("Here you can define the project in few sentences if you want.")
#         col1, col2 = st.columns([2, 4])
#         with col1:
#             project_name = st.text_input("Enter database name", key='project_name')
#         with col2:
#             project_description = st.text_area("Describe your data", key='project_description')
#         add_data_description = st.form_submit_button("Add project description", on_click=data_description_counter)


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
        column_table = pd.concat([column_table, pd.DataFrame({'table_name': [select_table], 'column_name': [column_name], 'column_description': [column_description], 'column_type': [column_type]})], ignore_index=True)
        st.session_state['column_table'] = column_table
        # refresh the page to see the changes
        st.experimental_rerun()

st.markdown("---")
st.markdown("## Data description")
st.markdown("### Tables that we have defined")
col1, col2 = st.columns([4, 2])
with col1:
    st.write(table_table)
with col2:
    with st.form(key='delete_table', clear_on_submit=True):
        st.markdown("### Delete table")
        st.markdown("Here we can delete a table that we have defined before.")
        select_table = st.selectbox("Select table", table_table['table_name'].astype(str).unique(), key='select_table_delete')
        delete_table = st.form_submit_button("Delete table", on_click=table_delete_counter)

st.markdown("### Columns that we have defined")
col1, col2 = st.columns([4, 2])
with col1:
    st.write(column_table)
with col2:
    column_unique_values = column_table['table_name'].astype(str) + ' --- ' + column_table['column_name'].astype(str)
    with st.form(key='delete_column', clear_on_submit=True):
        st.markdown("### Delete column")
        st.markdown("Here we can delete a column that we have defined before.")
        # concat table_name and column_name to get unique values
        select_column = st.selectbox("Select column", column_unique_values, key='select_column_delete')
        delete_column = st.form_submit_button("Delete column", on_click=column_delete_counter)

if st.session_state.table_delete_counter == 1:
    st.session_state.table_delete_counter = 0
    table_table = table_table[table_table['table_name'].astype(str) != select_table]
    st.session_state['table_table'] = table_table
    # refresh the page to see the changes
    st.experimental_rerun()

if st.session_state.column_delete_counter == 1:
    st.session_state.column_delete_counter = 0
    # split the unique value to get the table_name and column_name
    table_name, column_name = select_column.split(' --- ')
    # drop the row from the column_table where both of the values are the same as the selected values
    column_table = column_table[(column_table['table_name'].astype(str) != table_name) | (column_table['column_name'].astype(str) != column_name)]
    st.session_state['column_table'] = column_table
    # refresh the page to see the changes
    st.experimental_rerun()

st.markdown("***")

st.markdown("### Save the tables")
st.markdown("Here we can save the tables that we have defined as a pickle file.")
st.markdown("We can use the file to load the tables in the future.")

# create a dictionary with the table_table and the column_table and save it as a pickle file
combined_table = {'table_table': table_table,
                  'column_table': column_table}

datetime = pd.Timestamp.now().strftime("%Y-%m-%d_%H-%M-%S")

col1, col2 = st.columns([2, 1])

with col1:
    custom_filename = st.text_input("Enter custom filename if you want", key='file_name')
    if custom_filename != '':
        filename_to_use = f'{custom_filename}.pkl'
    else:
        filename_to_use = f'da_tool_export_{datetime}.pkl'
    download_tables = st.download_button(label="Download table structure for later",
                                         data=pickle.dumps(combined_table),
                                         file_name=filename_to_use,
                                         on_click=download_tables_counter)
    
st.session_state['combined_table'] = combined_table

st.markdown("---")
st.markdown("### Currently imported tables and columns")
st.markdown("Here we can see the tables and columns that our tool detects as imported.")
st.markdown("### Table table")
st.dataframe(combined_table['table_table'])
st.markdown("### Column table")
st.dataframe(combined_table['column_table'])

st.markdown("---")
st.markdown("Context for ChatGpt")
# make a dropdown with valuies: SQL, Pandas, R, Python
programing_language_options = ['SQL', 'Python', 'Python - Pandas', 'R']
if 'programing_language' not in st.session_state:
    st.session_state['programing_language'] = 'SQL'
    st.session_state['programing_language_counter'] = 0
programing_language = st.selectbox("Select programing language", programing_language_options,
                                   index=programing_language_options.index(st.session_state['programing_language']),
                                   key='programing_language_key', on_change=programing_language_counter)

if st.session_state.programing_language_counter == 1:
    st.session_state.programing_language_counter = 0
    st.session_state['programing_language'] = programing_language

full_string = ""
if programing_language == 'Python':
    introduction = f"""Hello I want you to help me to write code in {programing_language}. \n
I will give you the context and you need to write the code for me in {programing_language}.
In the context I will give you the table names, you can assume that it is already put in a pandas dataframe, you do not need to import them from the sql database.
I will also give you the table desciption and the list of columns in the table and the column description.
I want you to help me write the {programing_language} code.
I can run the code by myself.
The data contains the following pandas dataframes:\n\n"""
else:
    introduction = f"""Hello I want you to help me to write code in {programing_language}.
I will give you the context and you need to write the code for me in {programing_language}.
In the context I will give you the table names the table desciption and the list of columns and the column description.
I want you to help me write the code or the query that I need to get the data that I want.
I do not want the results, but the code that I can run myself.
The database contains the following tables:\n\n"""
full_string += introduction

for t in table_table['table_name'].unique():
    full_string += f"""The table that is called: '{t}' contains data about: {table_table[table_table['table_name'] == t]['table_description'].values[0]}.
It is already a pandas dataframe and has the following columns:\n\n"""
    for c in column_table[column_table['table_name'] == t]['column_name'].values:
        full_string += f"""* '{c}': """
        #  get the column description
        column_description = column_table[(column_table['table_name'] == t) & (column_table['column_name'] == c)]['column_description'].values[0]
        full_string += f"""which is {column_description}. \n\n"""
    full_string += f""" """

#st.text(full_string)

# save it to session state
st.session_state['full_string'] = full_string

