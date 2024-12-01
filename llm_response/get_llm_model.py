import os
from langchain_google_genai import ChatGoogleGenerativeAI
from config import CONFIG


def get_llm_model():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-001",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=CONFIG.gemini_api_key
    )
    return llm

