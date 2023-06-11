import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.da_functions import *
from PIL import Image
import plotly.graph_objects as go
import plotly.io as pio

st.set_page_config(layout='wide', page_title='Data Analysis Dashboard')
st.title("Test Chat GPT")
reset_response_list = st.sidebar.button("Reset response list")

def session_counter():
    # st.sesson counter intialization
    if 'session_counter' not in st.session_state:
        st.session_state.session_counter = 1
    st.session_state.session_counter = 1
    return st.session_state.session_counter

# Define tables
input_message = ""
with st.form(key='chat_gpt_form', clear_on_submit=True):
    text_input_for_chat_gpt = st.text_input("Enter your message here", input_message, key='chat_gpt_input')
    
    submitted = st.form_submit_button("Send to ChatGPT", on_click=session_counter)

if 'session_counter' not in st.session_state:
    st.session_state.session_counter = 0
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

# reset response list
if reset_response_list:
    user_input_list = []
    chatbot_response_list = []
    st.session_state['user_input_list'] = user_input_list
    st.session_state['chatbot_response_list'] = chatbot_response_list

if st.session_state.session_counter == 1:
    st.session_state.session_counter = 0
    response, _ = get_response_from_chat_gpt(text_input_for_chat_gpt)
    
    user_input_list.append(text_input_for_chat_gpt)
    chatbot_response_list.append(response)
     # append sessioin state list
    st.session_state.user_input_list = user_input_list
    st.session_state.chatbot_response_list = chatbot_response_list

    # reverse the lists
    user_input_list.reverse()
    chatbot_response_list.reverse()

    for i in range(len(user_input_list)):
        col1, col2, col3 = st.columns([1,12,1])
        with col1:
            st.markdown(f"**You:**")
        with col2:
            st.markdown(f"*{user_input_list[i]}*")
        with col1:
            st.markdown(f"**ChatGPT:**")
        with col2:
            st.markdown(f"*{chatbot_response_list[i]}*")

    


