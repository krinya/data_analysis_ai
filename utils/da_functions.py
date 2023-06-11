import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import json
import re

import openai
from openai.embeddings_utils import get_embedding, cosine_similarity

# ##Add API credential variables
# openai.api_base = open_ai_api_base
# openai.api_version = '2023-05-15'
openai.api_key = st.secrets['open_ai']['api_key']

def generate_answer_using_context(query, context=None, conversation=None):

    if conversation is None:
        conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": context},
        ]

    conversation.append({"role": "user", "content": query})

    response = openai.ChatCompletion.create(
        engine='ikea-gpt-35-turbo',
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


def get_response_from_chat_gpt(input):
    # here I would like to call the chatbot and get the response
    # put your code here
    answer, conversation = generate_answer_using_context(input, context=None, conversation=None)
    return answer, conversation