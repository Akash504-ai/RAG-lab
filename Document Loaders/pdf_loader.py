from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('CN_DBMS.pdf')

docs = loader.load()

# print(len(docs))                   # Number of pages
# print(docs[0])                     # First page document
# print(docs[0].page_content)        # First page text
# print(docs[0].metadata)             # First page metadata

