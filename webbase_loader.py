
from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)
url = "https://www.flipkart.com/apple-macbook-air-m5-2026-m5-16-gb-512-gb-ssd-tahoe-mdhe4hn-a/p/itm8505e2f874525"

loader = WebBaseLoader(url)

docs = loader.load()

context = "\n\n".join(
    doc.page_content for doc in docs
)

if not context.strip():
    raise ValueError("No website content extracted!")

print("Website loaded successfully!")

prompt = PromptTemplate(
    template="""
You are a helpful product information assistant.

Answer the user's question using ONLY the provided website content.

If the answer is not available in the website content,
clearly say that the information is not available.

Website Content:
{context}

User Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)

chain = prompt | model | StrOutputParser()

while True:

    question = input("\nAsk your question (type exit to stop): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = chain.invoke({
        "context": context,
        "question": question
    })

    print("\nAnswer:", response)