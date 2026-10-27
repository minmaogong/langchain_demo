# 1. 读取环境变量中的信息
from dotenv import load_dotenv
import os

from openai.types.responses import WebSearchPreviewToolParam

load_dotenv()
base_url = os.getenv("OPENAI_BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")

# 2. 创建对象
from openai import OpenAI
llm = OpenAI(
    base_url=base_url,
    api_key=api_key
)

# 3. 调用对象方法
res = llm.responses.create(
    model="gpt-4o-mini",
    input="2026年10月27日中国国内有哪些新闻，给我总结一下",
    tools=[WebSearchPreviewToolParam(type="web_search_preview")]
)

# 4. 输出结果
print(res.output_text)
