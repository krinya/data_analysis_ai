import streamlit as st
from PIL import Image
import os
import datetime
import pytz
import base64

st.set_page_config(layout='wide', page_title='Data Analysis Dashboard')

st.markdown("# Data Analysis Dashboard - Starting Page")
st.markdown("The code of the dashboard was last updated on: ")
# get the latest update from the github repo
os.path.getmtime('pages')
# convert it to datetime and set it to Amsterdam timezone
last_update = datetime.datetime.fromtimestamp(os.path.getmtime('pages'))
last_update = last_update.astimezone(tz=pytz.timezone('Europe/Amsterdam'))
# get only the date
last_update = last_update.date()
st.write(last_update)