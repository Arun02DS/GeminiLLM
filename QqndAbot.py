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
    return response

st.set_page_config(page_title="Contact with us", page_icon="🎧", layout="centered",)

st.header("Gemini LLM Application")

#Initailize the process for chat history
if 'chat_history' not in st.session_state:
    st.session_state["chat_history"]=[]

input=st.text_input("Input: ",key="input" )

submit = st.button("Ask?")

if submit and input:
    response = get_responce(input)
    st.session_state["chat_history"].append(["you",input])
    st.subheader("Qurey response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(["Bot",chunk.text])

st.subheader("chat history is")

for role,text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")

    # st.write(response)




