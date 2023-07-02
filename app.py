import streamlit as st
from PIL import Image
import os
import datetime
import pytz
import base64

st.set_page_config(layout='wide', page_title='Data Analysis Dashboard')

def openai_api_key_counter():
    # st.sesson counter intialization
    if 'openai_api_key_counter' not in st.session_state:
        st.session_state.openai_api_key_counter = 1
    st.session_state.openai_api_key_counter = 1
    return st.session_state.openai_api_key_counter

def openai_api_key_counter_sidebar():
    # st.sesson counter intialization
    if 'openai_api_key_counter_sidebar' not in st.session_state:
        st.session_state.openai_api_key_counter_sidebar = 1
    st.session_state.openai_api_key_counter_sidebar = 1
    return st.session_state.openai_api_key_counter_sidebar

if 'openai_api_key' not in st.session_state:
    openai_api_key = ""
    st.session_state['openai_api_key'] = openai_api_key
if 'openai_api_key_sidebar' not in st.session_state:
    openai_api_key_sidebar = ""
    st.session_state['openai_api_key_sidebar'] = openai_api_key_sidebar

st.markdown("# Welcome to Tablesense")
st.markdown("## The dasboard that helps you with your data analysis")
st.markdown("This dashboard is created to help you to wire queries and scripts. It uses Chat GPT in the backbround.")
st.markdown("It helps you to give answers to your coding questions based on the data that you have. Imagine as a Chat GPT, but better because it knows your data structure too.")
st.markdown(f"""
            So for example, once you configure it, you can ask questions like:  
            - How to write an SQL query to calculate my website visitors per day?
            - How to write a Python script to calculate the number of items sold per day?
            - Or even more complex questions like: How to write a Python script to calculate the number of items sold per day for each country?
            - Do EDA on my data using pandas and plotly express using the data that it is defined.
            """)
st.markdown("And it will give you the answer. If you do not like the result you can continue the conversation with the chatbot and it will give you a new answer.")
st.markdown("### How to use the dashboard?")

st.markdown("#### 1. Get your OpenAI API key, and give it to the dashboard.")
st.markdown(f"""In order to intaract with the dashboard (otherwise it won't work) first you need to have an OpenAI API key.
            Do not worry, it is prety easy to get one. Register at the Open AI page and add a a credit / debit card.
            Unfortunately using the API of the Chat GPT is not free, it costs some money for the API calls.
            But do not worry so much about it, it is not expensive. I used it for a while and it costs cents not even dollars.""")
st.markdown(f"""You can create the API key on https://beta.openai.com/account/api-keys.
            Once you create it you can copy it here below or to the sidebar to be able to use the dashboard""")


col1, col2 = st.columns([1,1])
with col1:
    with st.form(key='openai_api_key_form', clear_on_submit=True):
        openai_api_key = st.text_input("OpenAI API key", "", key= "openai_api_key_form")
        open_ai_submited_key = st.form_submit_button("Submit", on_click=openai_api_key_counter)

with st.sidebar:
    with st.form(key='openai_api_key_form_sidebar', clear_on_submit=True):
        openai_api_key_sidebar = st.text_input("OpenAI API key", "", key='openai_api_key_sidebar')
        open_ai_submited_key_sidebar = st.form_submit_button("Submit", on_click=openai_api_key_counter_sidebar)
        st.markdown(f"""<p style= "font-size: 10px;">Your Open AI API key: <br>
                    <b>{st.session_state['openai_api_key']}</b></p>
                    """, unsafe_allow_html=True)

if 'openai_api_key_counter' not in st.session_state:
    st.session_state.openai_api_key_counter = 0
if 'openai_api_key_counter_sidebar' not in st.session_state:
    st.session_state.openai_api_key_counter_sidebar = 0


if st.session_state.openai_api_key_counter == 1:
    st.session_state.openai_api_key_counter = 0
    st.session_state['openai_api_key'] = openai_api_key

if st.session_state.openai_api_key_counter_sidebar == 1:
    st.session_state.openai_api_key_counter_sidebar = 0
    st.session_state['openai_api_key'] = openai_api_key_sidebar

st.markdown("Your saved OpenAI API key:")
st.markdown(f"""
            <b>{st.session_state['openai_api_key']}</b>
            """, unsafe_allow_html=True)
st.markdown(f"""
            Do not forget to save it somewhere on your local machine too in a text file, because you might need it in the future!
            And you wont be able to access it from the same page again)
            """)

st.markdown("#### 2. Define your tables at the 'Define data' page.")
st.markdown("In order to be able to ask questions you need to define your tables. You can do it at the 'Define data' page.")
st.markdown("You can do this either importing a CSV file or add your data manualy by defining the table names and the column names of the tables")
st.markdown("Once you define the tables and the columns you can save it for latter use. Once you saved it you can load it later on the 'Load data' page.")
st.markdown("(The dashboard do not share this data with anyone, it is stored on your local machine for only a given session.)")

st.markdown("#### 3. Ask your questions in the Chat tab.")
st.markdown("Once you have your tables defined you can ask questions in the 'Talk with Chat GPT' page. Where you ask your questions and the Chat GPT will give you the answer.")

folder_path = 'pages'
latest_date = None

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        file_mtime = file_mtime.astimezone(pytz.timezone('Europe/Amsterdam')).date()
        
        if latest_date is None or file_mtime > latest_date:
            latest_date = file_mtime
st.sidebar.markdown("The code of the dashboard was last updated on: ")
st.sidebar.write(latest_date)


