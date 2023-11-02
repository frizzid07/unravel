import dotenv
import os
from langchain.document_loaders import PyPDFLoader

dotenv.load_dotenv()

loader = PyPDFLoader(
    file_path=os.getenv("PDF_PATH")
)

doc = loader.load()
print(doc)