from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langchain_groq import ChatGroq
# from langchain_community.llms import Ollama

from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

##for langsmith tracing
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# define the FastAPI app
app = FastAPI(
    title="Langchain Demo With Groq API llama-3.3-70b-versatile",
    description="Langchain Demo With Groq API llama-3.3-70b-versatile",
    version="0.1.0"
)

# Define your prompt template
prompt_template = ChatPromptTemplate.from_template(
    "Your prompt here with {topic}"
)

finance_prompt = ChatPromptTemplate.from_template(
    """
    Your are a financial advisor. helping the client to make the right investment decision. about this {topic}
    """
)

healthcare_prompt = ChatPromptTemplate.from_template(
    """
    Your are a healthcare professional. helping the client to make the right health decision. about this {topic}
    """
)

technology_prompt = ChatPromptTemplate.from_template(
    """
    Your are a technology professional. helping the client to make the right technology decision. about this {topic}
    """
)


llms = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.4,
)

add_routes(
    app,
    prompt_template|llms,
    path="/chat"
)

add_routes(
    app,
    finance_prompt|llms,
    path="/chat/finance"
)

add_routes(
    app,
    healthcare_prompt|llms,
    path="/chat/healthcare"
)

add_routes(
    app,
    technology_prompt|llms,
    path="/chat/technology"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)