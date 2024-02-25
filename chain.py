try:
    print(['pip', 'install', '-r', 'requirements.txt'])
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
except Exception as e: 
    print('installing requirements',e)

import os
from langchain.document_loaders.pdf import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv

# load_dotenv()

def chatbot_chain():
    loader = PyPDFLoader(file_path="bc1_cc3_merged.pdf")
    documents = loader.load()
    vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(),
                                                  retriever=vectorstore.as_retriever(),
                                                  memory=memory)
    return chain
