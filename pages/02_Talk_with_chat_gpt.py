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

# Define tables

text_input_for_chat_gpt = st.text_input("Enter your message here", "Type here...")
if st.button("Send"):
    response = get_response_from_chat_gpt(text_input_for_chat_gpt)
    st.write(response)


