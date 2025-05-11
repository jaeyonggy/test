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

def mock_web_search(query: str) -> str:
    return f"I don't know anything about: '{query}'"

web_search = Tool.from_function(
    name="web_search",
    func=mock_web_search,
    description="Useful for answering questions about current events or general world knowledge."
)


research_agent = create_react_agent(
    model=llm,
    tools=[web_search],
    prompt=(
        "You are a research agent.\n\n"
        "INSTRUCTIONS:\n"
        "- Assist ONLY with research-related tasks, DO NOT do any math\n"
        "- After you're done with your tasks, respond to the supervisor directly\n"
        "- Respond ONLY with the results of your work, do NOT include ANY other text."
    ),
    name="research_agent",
)