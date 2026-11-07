from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

# print(docs)
# print(len(docs))
print(docs[0])