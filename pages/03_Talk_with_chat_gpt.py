import streamlit as st
import pandas as pd
import numpy as np
from utils.da_functions import *
from PIL import Image

st.set_page_config(layout='wide', page_title='Data Analysis Dashboard')
st.title("Talk with Chat GPT")

# get context
if 'full_string' not in st.session_state:
    st.session_state.full_string = ""
    context_from_other_pages = st.session_state.full_string
else:
    context_from_other_pages = st.session_state.full_string

if 'previus_conversations' not in st.session_state:
    st.session_state.previus_conversations = ""
    previus_conversations = st.session_state.previus_conversations
else:
    previus_conversations = st.session_state.previus_conversations

if context_from_other_pages == "":
    st.warning(f"""Please define the data first, because there is no context yet.""")

reset_response_list = st.sidebar.button("Clear response list")
st.sidebar.markdown("Press this if you do not want to see the previus conversations in the chat.")
reset_previus_conversations = st.sidebar.button("Clear previus conversations")
st.sidebar.markdown("Press this if you do not want to give the previus conversations as context.")

def session_counter():
    # st.sesson counter intialization
    if 'session_counter' not in st.session_state:
        st.session_state.session_counter = 1
    st.session_state.session_counter = 1
    return st.session_state.session_counter

# Define tables
input_message = ""
with st.form(key='chat_gpt_form', clear_on_submit=True):
    #st.markdown("Message")
    text_input_for_chat_gpt = st.text_area("Enter your message or question here related to the data. This will be sent to the chat bot.", input_message, key='chat_gpt_input')
    #st.markdown("Context")
    #context_input = st.text_area("Enter your context here", input_message, key='chat_gpt_context')
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

# reset previus conversations
if reset_previus_conversations:
    previus_conversations = ""
    st.session_state['previus_conversations'] = previus_conversations

if st.session_state.session_counter == 1:
    st.session_state.session_counter = 0
    with st.spinner('Wait for it...'):
        # generate answer
        response, _ = generate_answer_using_context(text_input_for_chat_gpt, context_from_other_pages, st.session_state.previus_conversations)
        user_input_list.append(text_input_for_chat_gpt)
        chatbot_response_list.append(response)
        # append sessioin state list
        st.session_state.user_input_list = user_input_list
        st.session_state.chatbot_response_list = chatbot_response_list

        # reverse the lists
        user_input_list_reverse = user_input_list[::-1]
        chatbot_response_list_reverse = chatbot_response_list[::-1]
        for i in range(len(user_input_list)):
            col1, col2, col3 = st.columns([1,12,1])
            with col1:
                st.markdown(f""":thinking_face:""" + f""" <b>You</b>""", unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                            <b>{user_input_list_reverse[i]}</b>
                            """, unsafe_allow_html=True)
            with col1:
                st.markdown(f""":robot_face:""" + f"""**ChatGPT:**""", unsafe_allow_html=True)
            with col2:
                st.markdown(f"""{chatbot_response_list_reverse[i]}""", unsafe_allow_html=True)
            st.markdown("---")

        st.sidebar.markdown(f"""Monitor you costs on the folowing link [here](https://platform.openai.com/account/usage)""")
if st.session_state.session_counter == 0:
    user_input_list = st.session_state.user_input_list
    chatbot_response_list = st.session_state.chatbot_response_list
    user_input_list_reverse = user_input_list[::-1]
    chatbot_response_list_reverse = chatbot_response_list[::-1]
    for i in range(len(user_input_list)):
        col1, col2, col3 = st.columns([1,12,1])
        with col1:
            st.markdown(f""":thinking_face:""" + f""" <b>You</b>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                        <b>{user_input_list_reverse[i]}</b>
                        """, unsafe_allow_html=True)
        with col1:
            st.markdown(f""":robot_face:""" + f"""**ChatGPT:**""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""{chatbot_response_list_reverse[i]}""", unsafe_allow_html=True)
        st.markdown("---")

