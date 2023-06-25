import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import json
import re
import openai
#from openai.embeddings_utils import get_embedding, cosine_similarity

# ##Add API credential variables
# openai.api_base = open_ai_api_base
# openai.api_version = '2023-05-15'

def generate_answer_using_context(query, context=None, conversation=None):

    try:
        openai.api_key = st.secrets['open_ai']['api_key']
        api_key_custom_input = st.secrets['open_ai']['api_key']
    except:
        openai.api_key  = st.session_state['openai_api_key']
        api_key_custom_input = st.session_state['openai_api_key']

    if api_key_custom_input == "":
        st.error("Please enter your OpenAI API key on the front page.")
        return "No API key entered.", "No API key entered."

    if conversation is None:
        conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": context},
        ]

    conversation.append({"role": "user", "content": query})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=conversation,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    answer_message = response['choices'][0]['message']
    conversation.append(answer_message)

    return answer_message['content'], conversation

def get_response_from_chat_gpt(input, context=None):
    # call the chatbot and get the response
    if context:
        context_in=context
    else:
        context_in=""

    answer, conversation = generate_answer_using_context(input, context=context_in, conversation=None)
    return answer, conversation
