from langchain_ollama import ChatOllama

ollama_llm = ChatOllama(
    model="qwen3:8b",  # 模型名称
    base_url="http://localhost:11434", # 11434 是 Ollama 的默认端口
)

messages = [{
    "role": "user",
    "content": "你好，请介绍一下自己"
}]

res = ollama_llm.invoke(messages)

print(res.content)
