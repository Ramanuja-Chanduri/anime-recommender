from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from config.config import config

class VectorStoreBuilder:
    def __init__(self, csv_path: str, persist_directory: str):
        self.csv_path = csv_path
        self.persist_directory = persist_directory
        self.embedding = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)

    def build_and_save_vector_store(self):
        # Load documents from CSV
        loader = CSVLoader(file_path=self.csv_path, encoding='utf-8')
        documents = loader.load()

        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
        chunks = text_splitter.split_documents(documents)

        # Create and persist the vector store
        vector_store = Chroma.from_documents(
            chunks,
            self.embedding,
            persist_directory=self.persist_directory
        )
        
    def load_vector_store(self):
        return Chroma(
            embedding_function=self.embedding,
            persist_directory=self.persist_directory
        )