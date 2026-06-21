import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

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


response = llm.invoke("What is the capital of France?")
print("######## Text response ########")
print(response.text)

print("######## LLM Token Cost ########")
print(response.usage_metadata)

# Calculate the cost of the response
input_tokens = response.usage_metadata["input_tokens"]
output_tokens = response.usage_metadata["output_tokens"]

input_cost = input_tokens * 1.25 / 1000000
output_cost = output_tokens * 2.50 / 1000000

total_cost = input_cost + output_cost
# keep it in readable format
total_cost = f"{total_cost:.6f}"

print("######## Total Cost ########")
print(f"${total_cost}")
