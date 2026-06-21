# SystemMessage: instructions that control assistant behaviour
# HumanMessage: user input
# AIMessage: model response
# ToolMessage: result returned by a tool


import os 
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain.messages import SystemMessage, HumanMessage
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

messages = [
    SystemMessage(content="You are a helpful assistant that can answer questions and help with tasks."),
    HumanMessage(content="What is the capital of France?"),
]

response = llm.invoke(messages)
print(response.text)