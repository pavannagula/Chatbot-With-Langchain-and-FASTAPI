from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_mistralai.chat_models import ChatMistralAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['MISTRAL_API_KEY'] = os.getenv('MISTRAL_API_KEY')

app = FastAPI(
    title= "Langchain Server",
    version= "1.0",
    description= "An API Server"
)

add_routes(
    app, 
    ChatMistralAI(), 
    path="/openapi"
)

Mistral_model = ChatMistralAI()

#llama 3
llama_model = Ollama(model="llama3")

prompt1 = ChatPromptTemplate.from_template("Explain me about the {topic} within 250 words")
prompt2 = ChatPromptTemplate.from_template("Explain me about the {topic} and give examples within 250 words")

add_routes(
    app, 
    prompt1|Mistral_model,
    path = "/essay"
)

add_routes(
    app, 
    prompt2|llama_model,
    path = "/examples"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)