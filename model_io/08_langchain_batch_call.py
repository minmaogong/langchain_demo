from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()

llm = init_chat_model(
    model="gpt-4o-mini",  # 模型名称
    model_provider="openai",  # 模型提供商
)

# 批次调用
res = llm.batch(
    inputs=[
        "什么是Langchain?",
        "什么是RAG?",
        "什么是Agent?"
    ]
)

for message in res:
    print(message.content)
