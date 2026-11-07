from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return self.name

    def get_age(self):
        return self.age


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def get_subject(self):
        return self.subject
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=150,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)
    print("Length:", len(chunk))
