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


# Mock RAG 버전
def car_info_search(query: str) -> str:
    with open("rag/g80_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return json.dumps(data, ensure_ascii=False)  # Return full data



car_info_search = Tool.from_function(
    name="car_info_search",
    func=car_info_search,
    description=(
        "차량에 대한 정보를 찾을 때 쓰는 도구입니다.\n"
        "차량 가격, 트림 종류, 옵션 구성, 외장/내장 색상 등과 관련된 질문에 답하기 위해 이 도구를 사용하세요."
    )
)


car_info_agent = create_react_agent(
    model=llm,
    tools=[car_info_search],
    prompt=(
        "당신은 차량에 대한 전문 지식을 갖춘 Car Info Agent입니다.  \n\n"
        "INSTRUCTIONS:\n"
        "- 사용 가능한 도구를 활용해 차량 가격, 트림, 사양, 옵션 등에 관한 모든 질문에 정확하게 답해야 합니다.\n"
        "- 예를 들어 사용자가 제네시스 G80과 같은 특정 모델에 대해 물어보면, 관련 도구를 호출하여 구조화된 최신 정보를 제공하세요.\n"
        "- 답변은 간결하면서도 유익해야 하며, 추측보다는 최신의 정확한 데이터를 우선시해야 합니다."
        "- Respond ONLY with the results of your work, do NOT include ANY other text."
    ),
    name="car_info_agent",
)




