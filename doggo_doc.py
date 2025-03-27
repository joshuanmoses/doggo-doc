import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
import gradio as gr

#Load PDFs
pdf_paths = ["vet1.pdf", "vet2.pdf", "vet3.pdf", "vet4.pdf"]
all_docs = []

for path in pdf_paths:
    if os.path.exists(path):
        loader = PyPDFLoader(path)
        all_docs.extend(loader.load())
    else:
        print(f"⚠️ File not found: {path}")

#Chunk the documents
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(all_docs)

#Generate embeddings & store in FAISS
print("🔄 Creating embeddings...")
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(chunks, embedding)
db.save_local("doggo_doc_db")

#Set up QA with Ollama LLM
print("🔌 Loading vector DB and connecting to Ollama...")
db = FAISS.load_local("doggo_doc_db", embedding)
llm = Ollama(model="mistral")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

#Gradio chatbot
def ask_doggo(query):
    return qa_chain.run(query)

print("🚀 Launching Doggo Doc...")

gr.Interface(
    fn=ask_doggo,
    inputs=gr.Textbox(lines=2, placeholder="Ask something about veterinary medicine..."),
    outputs="text",
    title="🐶 Doggo Doc - Veterinary Medicine Assistant",
    description="Ask questions about canine health based on your veterinary PDFs."
).launch()
