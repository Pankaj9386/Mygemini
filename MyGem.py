import streamlit as st
import google.generativeai as genai


import os
st.title("MYGemini")
st.header("Ask question",divider='rainbow')
API_KEY = "your api key"
genai.configure(api_key=API_KEY)
generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

chat_session = model.start_chat(history=[])
    # newresponse=model.generate_content()

def get_gemini_answer(question):
    response = chat_session.send_message(question,stream=True)
    return response

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
    
input=st.text_input("Enter the question: ",key="input")
submit=st.button("get response")


if submit and input:
    response=get_gemini_answer(input)
    st.session_state['chat_history'].append(("You prompt",input))
    st.subheader("response: ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("MyGemini",chunk.text))
        
    st.subheader("Chat history")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
    
