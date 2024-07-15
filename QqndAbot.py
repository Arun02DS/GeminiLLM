from dotenv import load_dotenv
load_dotenv()  # loading environment variable.

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Gemini pro model load

model=genai.GenerativeModel("gemini-pro")

chat=model.start_chat(history=[])

def get_responce(prompt):
    response = chat.send_message(prompt,stream=True)
    return response.text

st.set_page_config(page_title="Contact with us", page_icon="🎧", layout="centered",)

st.header("Gemini LLM Application")

#Initailize the process for chat history
if ''




