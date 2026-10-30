from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

# 1. 加载文档
# 1.1 创建文档加载器
loader = UnstructuredWordDocumentLoader(
    file_path="../assets/sample.docx",
    mode="single",  # 解析模式，"single"表示将文档解析为单个元素
    encoding="utf-8"
)
# 1.2 调用load方法
documents = loader.load()

# 2. 切分文档：按照固定的字符进行切分
# 2.1 创建切分器对象
splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", "。", "！", "？", "……"], # 分隔符列表
    chunk_size=400,  # 每个块的最大长度
    chunk_overlap=50,  # 每个块重叠的长度
    length_function=len, # 可选：计算文本长度的函数，默认为字符串长度，可自定义函数来实现按 token 数切分
    add_start_index=True # 可选：块的元数据中添加此块起始索引
)
# 2.2 调用切分方法
chunks = splitter.split_documents(documents)

for chunk in chunks:
    print(chunk, end="\n\n" + "=" * 150 + "\n\n")
