import requests
import streamlit as st 

def get_mistralai_response(input):
    response = requests.post("https://localhost:8000/essay/invoke",
    json = {'input': {'topic':input}})

    return response.json()['output']['content']

def get_ollama_response(input):
    response = requests.post("https://localhost:8000/examples/invoke",
    json = {'input': {'topic':input}})

    return response.json()['output']['content']

## streamlit
st.title('Chatbot with Mistral AI and Llama3')
input=st.text_input("Write an essay on")
input1=st.text_input("provide some examples on")

if input:
    st.write(get_mistralai_response(input))

if input1:
    st.write(get_ollama_response(input1))
