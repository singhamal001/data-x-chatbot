# CryptoCompass: Navigate the World of Cryptocurrency

## Overview

CryptoCompass is an innovative application designed to demystify the complex world of cryptocurrency for enthusiasts and investors alike. Leveraging the power of Retriever-Augmented Generation (RAG) and Language Learning Models (LLMs), CryptoCompass provides accurate, up-to-date information and answers to a wide range of crypto-related questions. Whether you're curious about blockchain basics, the nuances of various cryptocurrencies, or the latest trends in DeFi and NFTs, CryptoCompass is here to guide you.

## Features

- **Comprehensive Crypto Knowledgebase:** Access to a wide array of cryptocurrency topics including Bitcoin, Ethereum, blockchain technology, DeFi, NFTs, cryptocurrency trading, investment strategies, and more.
- **Interactive Q&A:** Engages users in a conversational manner, offering precise answers and personalized recommendations.
- **Multi-Platform Support:** Deployable across various platforms such as websites, mobile applications, and social media for easy access.
- **User-Friendly Design:** Built with Streamlit, the app offers a clean, intuitive interface for users of all levels.
- **Innovative Technology:** Powered by a combination of RAG and LLM, CryptoCompass delivers precise and contextually relevant answers.

## Installation

### Prerequisites

- Python 3.8 or newer
- pip or conda

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/singhamal001/data-x-chatbot.git
    cd data-x-chatbot
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the chatbot, run the following command in your terminal:

```bash
python -m streamlit run app.py
```

Once the chatbot is running, you can interact with it by typing your questions into the console. The bot will process your query and return an answer related to cryptocurrency.

## Acknowledgments

- OpenAI for the RAG model.
- Open-source information from the web for information related to cryptocurrencies.

---

## How to Interact with CryptoCompass

1. **Start a Conversation:** Simply launch the app and you'll be greeted by the CryptoCompass chatbot, ready to answer your questions.
2. **Ask Your Question:** Use the chat input to type your cryptocurrency-related question and hit enter.
3. **Receive Instant Answers:** The chatbot, powered by our sophisticated RAG-based chain model, will provide you with a detailed answer.
4. **Explore Further:** Don't hesitate to ask follow-up questions or explore different topics within the cryptocurrency domain.

## Behind the Scenes: Technical Innovations

CryptoCompass is powered by a custom-built `chatbot_chain` that integrates RAG and LLM technologies. This backend, built in Python, leverages:

- **PyPDFLoader** for ingesting cryptocurrency-related documents, providing a rich knowledge base.
- **OpenAIEmbeddings** and **FAISS** vector storage for efficient retrieval of relevant information based on your query.
- **ChatOpenAI** model for generating coherent, contextually relevant answers.
- **ConversationBufferMemory** for a seamless conversational experience, remembering the context of the interaction.

This advanced setup ensures that CryptoCompass can provide highly accurate and context-aware answers to your queries, making it a cutting-edge tool in the crypto space.

## Acknowledgments

- **Streamlit:** For the intuitive app framework that enhances user experience.
- **OpenAI:** For the foundational models and embeddings that power our chatbot.
- **FAISS & PyPDFLoader:** For enabling efficient document retrieval and processing.

CryptoCompass stands at the intersection of technology and finance, offering a unique tool for anyone looking to navigate the cryptocurrency landscape with ease and confidence.
