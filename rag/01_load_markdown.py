# 1. 创建加载器对象
from langchain_community.document_loaders import UnstructuredMarkdownLoader
loader = UnstructuredMarkdownLoader(
    file_path="../assets/sample.md",
    mode="elements",  # 解析模式，"elements"表示将文档解析为元素列表
    encoding="utf-8"
)

# 2. 调用加载器对象的方法进行文档加载
docs = loader.load()

# 3. 输出加载后的结果
for doc in docs:
    print(doc.page_content + "\n")
    print("=====================================")
