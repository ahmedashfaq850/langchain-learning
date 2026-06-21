import os
from dotenv import load_dotenv
from langchain.messages import HumanMessage, SystemMessage
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
model_name = os.getenv("OPENROUTER_MODEL")

if not api_key or not model_name:
    raise ValueError("OPENROUTER_API_KEY and OPENROUTER_MODEL must be set")

llm = ChatOpenRouter(
    model = model_name,
    api_key = api_key,
    temperature = 0.0,
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant that can answer questions and help with tasks."
    ),
    (
        "human",
        "What is the capital of {input}?"
    )
])

formatted_prompt = prompt.invoke(input="France")
response = llm.invoke(formatted_prompt)
print(response.text)