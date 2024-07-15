from dotenv import load_dotenv
load_dotenv()  # loading environment variable.

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Gemini pro model load

model=genai.GenerativeModel("gemini-pro")

def get_responce(prompt):
    response = model.generate_content(prompt)
    return response.text

# st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

# page configuration

st.set_page_config(page_title="Contact with us", page_icon="🎧", layout="centered",)

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input" )

submit = st.button("How may I help You?")

if submit:
    response = get_responce(input)
    st.subheader("Qurey response:")
    st.write(response)




