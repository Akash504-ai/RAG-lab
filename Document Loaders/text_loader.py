from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

loader = TextLoader('cricket.txt', encoding='utf-8')
docs = loader.load()

prompt = PromptTemplate(
    template="Summarize the following document in simple language:\n\n{text}",
    input_variables=["text"]
)

chain = prompt | model | StrOutputParser()

document_text = docs[0].page_content
                          
summary = chain.invoke({"text": document_text})

print("Document Summary:")
print(summary)