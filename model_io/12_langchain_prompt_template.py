from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

def prompt_template_demo(product: str, aspect1: str, aspect2: str) -> None:
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # 模型名称
    )

    # 定义提示词模版
    # chat_prompt_template = ChatPromptTemplate([
    #     SystemMessage(content="你是一个专业的评论员"),
    #     {"role": "user", "content": "请评价{product}的优缺点，包括{aspect1}和{aspect2}两方面。"}
    # ])
    # 必须使用元组格式("role", "模版字符串" 才能进行变量替换)
    # 若使用 SystemMessage/HumanMessage 直接传入，会被当作普通消息，{变量} 不会被替换
    chat_prompt_template = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的评论员"),
        ("human", "请评价{product}的优缺点，包括{aspect1}和{aspect2}两方面。")
    ])

    # PromptValue
    prompt = chat_prompt_template.invoke(
        input={
            "product": product,
            "aspect1": aspect1,
            "aspect2": aspect2
        }
    )

    print(prompt)

    res = llm.invoke(
        input=prompt
    )
    print(res)

if __name__ == "__main__":
    prompt_template_demo(product="iPhone 15", aspect1="性能", aspect2="价格")
