# Doggo Doc by Joshua Moses
print("Doggo Doc by Joshua Moses")

#Install dependencies
print("Installing Dependencies")
sudo pip install langchain faiss-cpu openai chromadb pypdf gradio llama-cpp-python sentence-transformers langchain-community

# langchain - llm framework
# faiss-cpu - a library for efficient similarity search and clustering of dense vectors
# openai - openai API
# chromadb - db for storing and retrieving vector embeddings
# pypdf - library for manipulating PDF files
# gradio - web interface
# llama-cpp-python - binding libraries for llama
# sentence-transformers - encodes sentences into fixed-length vectors
# langchain-community - 3rd party libraries for langchain


# install and run the model
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral

print("Make sure to put all the PDF's in the same directory as the script and rename them to vet1.pdf, vet2.pdf, vet3.pdf and vet4.pdf")
#Put all the pdfs in the same directory as the script and rename them:
#vet1.pdf
#vet2.pdf
#vet3.pdf
#vet4.pdf

#run it
python3 doggo_doc.py