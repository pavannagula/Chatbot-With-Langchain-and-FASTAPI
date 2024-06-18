from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
import streamlit as st 

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "TRUE"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assisstant and answer user queries"),
        ("user","Question:{question}")
    ]
)

## Streamlit Template

st.title("Chatbot Application using Llama 3")
input_text = st.text_input("Ask any question")

## Llama 3 Model

llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
     st.write(chain.invoke({"question": input_text}))