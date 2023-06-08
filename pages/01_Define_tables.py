import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.da_functions import *
from PIL import Image
import plotly.graph_objects as go
import plotly.io as pio

st.set_page_config(layout='wide', page_title='Data Analysis Dashboard')
st.title("Define Tables")

# Load data
st.markdown("Here I would liek to define tagbles either manualy or by uplading a csv file")
st.markdown("The tables should have a name, e.g.: 'Transactions' or 'Customers' and a description")
st.markdown("Each table should have columns listed and be able to add a description")

# Define tables



