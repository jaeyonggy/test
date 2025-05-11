import os
from dotenv import load_dotenv
# Load variables from .env into os.environ
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-001",
    temperature=0,
    google_api_key=google_api_key
)

from langchain_core.tools import Tool
from langgraph.prebuilt import create_react_agent
import json

with open("prompts/profiler_system_prompt.txt", "r", encoding="utf-8") as f:
        profiler_system_prompt = f.read()

profiler_agent = create_react_agent(
    model=llm,
    tools=[],
    prompt=profiler_system_prompt,
    name="profiler_agent",
)




