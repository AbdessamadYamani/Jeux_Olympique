from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import fitz  # For PDF
from langchain.tools import tool
from langchain_openai import OpenAIEmbeddings
import os
import json

# Initialize OpenAIEmbeddings with API key
embedding_function = OpenAIEmbeddings(openai_api_key='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')

class BusinessAnalysisToolsClass:
    @tool("Content Loader")
    def load_content(query: str):
        """Charge et traite le contenu de Documentation - Web site"""
        global_retriever_results = []
        directory_path = r"C:\Users\abdes\Desktop\devpy\crewai-updated-tutorial-hierarchical\assets\Data"
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            if filename.endswith('.pdf'):
                # Processing for PDF files
                doc = fitz.open(file_path)
                text = [page.get_text() for page in doc]
                doc.close()
            elif filename.endswith('.json'):
                # Processing for JSON files
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    text = [item['html'] for item in data]  
                    if not isinstance(text, list):
                        text = [text]
            else:
                continue

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            splits = text_splitter.create_documents(text)
            if splits:
                vectorstore = Chroma.from_documents(splits, embedding=embedding_function, persist_directory="./chroma_db_babok")
                retriever = vectorstore.similarity_search(query)
                global_retriever_results.append(retriever)
            else:
                global_retriever_results.append("No content available for processing in " + filename)
        return global_retriever_results
