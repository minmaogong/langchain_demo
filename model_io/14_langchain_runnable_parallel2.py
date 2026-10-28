from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

"""
# 目标：用OpenAI模型，以及Google的模型对诗进行分析，然后将两个分析结果交给DeepSeek的模型及逆行总结评价
"""

load_dotenv()


def runnable_parallel_demo(poem: str) -> None:
    # 1. 提示词模板
    paragraph_1 = ChatPromptTemplate.from_messages([{"role":"user", "content":"对这首诗{poem}做一下赏析，分析它蕴含的含义"}])
    # 2. openai 模型
    openai_llm = ChatOpenAI(
        model="gpt-4o-mini",
    )
    # 3. 解析器
    str_output_parser = StrOutputParser()
    # 4. 调用链
    openai_chain = paragraph_1 | openai_llm | str_output_parser


    gemini_llm = ChatOpenAI(
        model="gemini-2.5-flash-lite",
    )
    gemini_chain = paragraph_1 | gemini_llm | str_output_parser

    paragraph_2 = ChatPromptTemplate.from_messages([{"role":"user", "content":"这两种赏析，第一种：{paragraph_1}，第二种：{paragraph_2}，哪个更好？为什么？"}])
    deepseek_llm = ChatOpenAI(
        model="deepseek-v4-flash",
    )
    deepseek_chain = paragraph_2 | deepseek_llm | str_output_parser

    # 组成并行调用链
    map_chain = {
        "paragraph_1": openai_chain,
        "paragraph_2": gemini_chain, # openai_chain 和 gemini_chain 并行调用链
    } | deepseek_chain # 等 openai_chain和gemini_chain 并行调用完成后，将结果传给 deepseek_chain

    res = map_chain.invoke({"poem": poem})
    print(res)


if __name__ == "__main__":
    poem = """
        菩提本无树，
        明镜亦非台，
        本来无一物，
        何处惹尘埃。
        """
    runnable_parallel_demo(poem=poem)
