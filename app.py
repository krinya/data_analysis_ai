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

st.markdown("# Data Analysis Dashboard - Starting Page")
st.markdown("The code of the dashboard was last updated on: ")
# convert it to datetime and set it to Amsterdam timezone

folder_path = 'pages'
latest_date = None

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        file_mtime = file_mtime.astimezone(pytz.timezone('Europe/Amsterdam')).date()
        
        if latest_date is None or file_mtime > latest_date:
            latest_date = file_mtime
st.write(latest_date)


st.markdown("### Give your OpenAI API key to be able to use the dashboard")
st.markdown(f"""You can create one on https://beta.openai.com/account/api-keys.
            Once you create it you can copy it and paste it in the field below.""")

col1, col2 = st.columns([1,1])
with col1:
    with st.form(key='openai_api_key_form', clear_on_submit=False):
        #st.markdown("Message")
        openai_api_key = st.text_input("OpenAI API key", "")
        open_ai_submited_key = st.form_submit_button("Submit", on_click=openai_api_key_counter)


if 'openai_api_key_counter' not in st.session_state:
    st.session_state.openai_api_key_counter = 0
if 'openai_api_key' not in st.session_state:
    openai_api_key = ""
    st.session_state['openai_api_key'] = openai_api_key

if st.session_state.openai_api_key_counter == 1:
    st.session_state.openai_api_key_counter = 0
    st.session_state['openai_api_key'] = openai_api_key

st.markdown("Your saved OpenAI API key:")
st.markdown(f"""**{st.session_state['openai_api_key']}**""")
st.markdown(f"""Do not forget to save it somewhere on your local machine in a text file as well, because you might need it in the future!))""")

