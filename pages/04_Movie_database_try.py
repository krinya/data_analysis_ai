# link: https://www.w3resource.com/sql-exercises/movie-database-exercise/joins-exercises-on-movie-database.php

import streamlit as st
import pandas as pd
import numpy as np
from utils.da_functions import *
from PIL import Image
import pickle

st.set_page_config(layout='wide', page_title='Data Analysis Dashboard')
st.title("Movie Database")

# ebade the link that I sent you in an iframe
st.markdown('<iframe src="https://www.w3resource.com/sql-exercises/movie-database-exercise/joins-exercises-on-movie-database.php" width="1000" height="800"></iframe>', unsafe_allow_html=True)