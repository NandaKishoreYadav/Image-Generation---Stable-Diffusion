import streamlit as st
from helper import *

st.set_page_config(page_title="Image Generation",page_icon='📸')
st.title('Image Generation')

prompt = st.text_input("Enter the Prompt")

image = helper.generate_image(prompt)

st.image(image, caption='Generated Image.', use_column_width=True)
