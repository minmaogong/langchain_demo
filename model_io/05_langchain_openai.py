from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

# 1. 创建对象
from dotenv import load_dotenv
import os
load_dotenv()
base_url = os.getenv("OPENAI_BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    model="gpt-4o-mini",  # 模型名称
    base_url=base_url,
    api_key=api_key,
    temperature=0.7, # 控制生成文本的随机性。数字越高，回答越有创意；数字低，回答越确定，涉及到大模型采样相关内容
)

# 2. 调用方法
# res = llm.invoke(input=[
#     {
#         "role": "system",
#         "content": "你是一名资深的美食博主，擅长分享美食制作技巧和餐厅推荐。"
#     },
#     {
#         "role": "user",
#         "content": "请推荐几家适合家庭聚餐的餐厅，并说明理由。"
#     }
# ])
import logging
logging.basicConfig(level=logging.DEBUG)
res = llm.invoke(input=[
    SystemMessage(content="你是一名资深的美食博主，擅长分享美食制作技巧和餐厅推荐。"),
    HumanMessage(content="九转大肠这道菜味道怎么样？")
])

print(type(res))
print(res.content)
