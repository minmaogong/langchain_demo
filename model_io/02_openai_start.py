from openai import OpenAI
from dotenv import load_dotenv
import os

# 向 OpenAI 大模型输入一句话，拿到OpenAI的输出，并且将输出打印出来
text = "什么是LangChain？"
# 1. 创建OpenAI大模型对象
# 获取api_key和base_url
load_dotenv()
base_url = os.getenv("OPENAI_BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(
    base_url=base_url,
    api_key=api_key
)

# 2. 调用对象的方法创建对话，拿到对话结果
res = llm.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "system",
        "content": "你是一名资深的大模型工程师，精通Python编程语言，熟悉LangChain框架，能够根据用户的需求，快速生成高质量的代码。"
    }, {
        "role": "user",
        "content": text
    }]
)

# 3. 打印结果
print(res.choices[0].message.content)
