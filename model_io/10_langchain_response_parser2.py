from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import logging

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",  # 模型名称
)

"""
{
    "prime":[1,2,3,4,5],
    "count":[1,2,3,4,5]
}
"""


class Prime(BaseModel):  # BaseModel 是 Pydantic 提供的基类，用于定义数据模型
    prime: list[int] = Field(description="素数")
    count: list[int] = Field(description="小于该素数的素数个数")

logging.basicConfig(level=logging.DEBUG)

# 2. 将大模型对象转成配置了结果解析的大模型对象
structured_llm = llm.with_structured_output(schema=Prime)

res = structured_llm.invoke(
    input=[{
        "role": "user",
        "content": "任意生成5个1000-100000之间素数，并标出小于改素数的素数个数"
    }])
print(res)
print(type(res))
print(res.prime)
print(res.count)
