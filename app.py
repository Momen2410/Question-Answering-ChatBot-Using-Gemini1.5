import google.generativeai as genai
import streamlit as st

API = input('Add Gemini 1.5 API to Chat: ')
genai.configure(api_key=API)
# Set up the model

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

def get_model_respose(question):
    model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                                generation_config=generation_config)

    convo = model.start_chat()
    

    respose = convo.send_message(question)
    respose = respose.text
    return respose

st.set_page_config(page_title = 'Q&A Demo')
st.header('Smart Chatbot Project Using Gemeini 1.5 API')

input = st.text_input('Chat', key = 'Chat')
response = get_model_respose(input)

submit = st.button('Send')

if submit:
    st.subheader('Answer:')
    st.write(response)