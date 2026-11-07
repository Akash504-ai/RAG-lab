from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
My name is Nitish.
I am 35 years old.

I live in Gurgaon.
How are you?
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=30,
    chunk_overlap=0,
    # separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(text)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    # print(f"\nChunk {i + 1}:")
    print(chunk)
    print("Length:", len(chunk))
