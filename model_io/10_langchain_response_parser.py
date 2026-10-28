from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
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

# 1. 创建JsonOutputParser 对象
json_output_parser = JsonOutputParser(pydantic_object=Prime)
print(json_output_parser.get_format_instructions()) # 根据定义 Prime 数据类，获取格式化的Prompt提示词指令，告诉模型输出的格式要求
res = llm.invoke(
    input=[{
        "role": "system",
        "content": json_output_parser.get_format_instructions()  # 获取格式化指令
    },{
        "role": "user",
        "content": "任意生成5个1000-100000之间素数，并标出小于改素数的素数个数"
    }])

print(res.content)
