import asyncio

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import time
import os

load_dotenv()
base_url = os.getenv("OPENAI_BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")

# 1. 模拟发送三个请求
MESSAGES = [
    "什么是Langchain?",
    "什么是RAG?",
    "什么是Agent?"
]

def call_llm_sync(messages: list[str]):
    # 2. 创建对象
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # 模型名称
        base_url=base_url,
        api_key=api_key,
        temperature=0.7, # 控制生成文本的随机性。数字越高，回答越有创意；数字低，回答越确定，涉及到大模型采样相关内容
    )
    # 记录时间
    time0 = time.perf_counter()
    for message in messages:
        llm.invoke(input=message)
    time1 = time.perf_counter()
    print(f"同步调用耗时: {time1 - time0:.2f} 秒")

async def call_llm_async(messages: list[str]):
    # 2. 创建对象
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # 模型名称
        base_url=base_url,
        api_key=api_key,
        temperature=0.7,  # 控制生成文本的随机性。数字越高，回答越有创意；数字低，回答越确定，涉及到大模型采样相关内容
    )
    # 记录时间
    time0 = time.perf_counter()
    task = [llm.ainvoke(input=message) for message in messages] # 返回的是一个协程对象列表，没有真正执行
    # asyncio.gather 并发执行
    await asyncio.gather(*task) # * -> 序列解包 ** -> 字典解包
    time1 = time.perf_counter()
    print(f"异步调用耗时: {time1 - time0:.2f} 秒")



if __name__ == "__main__":
    call_llm_sync(MESSAGES)
    # 执行异步调用
    asyncio.run(call_llm_async(MESSAGES) )
