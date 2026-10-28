from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def runnable_parallel_demo(topic: str) -> None:

    llm = ChatOpenAI(
        model="gpt-4o-mini",  # 模型名称
    )

    str_output_parser = StrOutputParser()

    english_prompt_template = PromptTemplate.from_template("把这个句子 {topic} 翻译成英文，只要翻译结果，不要其他内容")
    english_chain = english_prompt_template | llm | str_output_parser

    korean_prompt_template = PromptTemplate.from_template("把这个句子 {topic} 翻译成韩文，只要翻译结果，不要其他内容")
    korean_chain = korean_prompt_template | llm | str_output_parser

    # 组成并行调用链
    map_chain = RunnableParallel(english=english_chain, korean=korean_chain)

    res = map_chain.invoke({"topic": topic})
    print(res)

if __name__ == "__main__":
    runnable_parallel_demo(topic="人工智能是一种智能技术")
