# from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama
from langchain_groq import ChatGroq

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

##for langsmith tracing
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('Langchain Demo With Groq API llama-3.3-70b-versatile')
input_text=st.text_input("Search the topic u want...")

# ollama LLAma2 LLm
# llm=Ollama(model="llama2")


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    # max_retries=2,
    # other params...
)

output_parser=StrOutputParser()

chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))