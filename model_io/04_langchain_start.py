# langchain统一的这套api， init_chat_model
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
import os
load_dotenv()
base_url = os.getenv("OPENAI_BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")

# 1. 创建对象
llm = init_chat_model(
    model="gpt-4o-mini",  # 模型名称
    model_provider="openai",  # 模型提供商
    base_url=base_url,
    api_key=api_key
)

# 2. 调用方法创建对话
res = llm.invoke("你是谁?")

print(res)
