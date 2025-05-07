import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyC9_AXZVd5OCnVh8Fu5W_n0jJvUfMz9o5o"
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-001",
    temperature=0,
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

from langgraph_supervisor import create_supervisor
from agents.math_agent import math_agent
from agents.research_agent import research_agent

supervisor = create_supervisor(
    model=llm,
    agents=[research_agent, math_agent],
    prompt=(
        "You are a supervisor managing two agents:\n"
        "- a research agent. Assign research-related tasks to this agent\n"
        "- a math agent. Assign math-related tasks to this agent\n"
        "Assign work to one agent at a time, do not call agents in parallel.\n"
        "Do not do any work yourself."
    ),
    add_handoff_back_messages=True,
    output_mode="full_history",
).compile()