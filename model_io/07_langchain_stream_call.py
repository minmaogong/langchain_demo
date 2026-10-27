from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = init_chat_model(
    model="gpt-4o-mini",  # 模型名称
    model_provider="openai",  # 模型提供商
)

# 流式调用
res = llm.stream(input=[
    SystemMessage(content="你是一名资深狗仔队。"),
    HumanMessage(content="周杰伦和田馥甄有没有谈过恋爱？")
],)

for message in res:
    print(message.content, end="", flush=True) # end="" -> 不换行 flush=True -> 立即刷新输出缓冲区
