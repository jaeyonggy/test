import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyC9_AXZVd5OCnVh8Fu5W_n0jJvUfMz9o5o"
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-001",
    temperature=0,
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

from langchain_core.tools import Tool
from langgraph.prebuilt import create_react_agent

# Define the functions
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    return a / b

# Wrap the functions with Tool.from_function
add_tool = Tool.from_function(
    func=add,
    name="add",
    description="Add two numbers"
)

multiply_tool = Tool.from_function(
    func=multiply,
    name="multiply",
    description="Multiply two numbers"
)

divide_tool = Tool.from_function(
    func=divide,
    name="divide",
    description="Divide two numbers"
)

# Pass the tools to the agent
math_agent = create_react_agent(
    model=llm,
    tools=[add_tool, multiply_tool, divide_tool],
    prompt=(
        "You are a math agent.\n\n"
        "INSTRUCTIONS:\n"
        "- Assist ONLY with math-related tasks\n"
        "- After you're done with your tasks, respond to the supervisor directly\n"
        "- Respond ONLY with the results of your work, do NOT include ANY other text."
    ),
    name="math_agent",
)
