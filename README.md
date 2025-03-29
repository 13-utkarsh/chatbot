# Chatbot Setup Guide

This guide will help you set up and run the chatbot locally on your system.

## 1. Clone the Repository

```bash
git clone https://github.com/13-utkarsh/chatbot.git
cd chatbot
```

## 2. Clone the Documentation Repository

The chatbot uses markdown files from the Fossology wiki. Clone the wiki repository inside the project folder:

```bash
git clone https://github.com/fossology/fossology.wiki.git fossology-wiki
```

## 3. Install Ollama and Pull the Embedding Model

Download and install [Ollama](https://ollama.ai/), then pull the required embedding model:

```bash
ollama pull nomic-embed-text
```

## 4. Create a Python Virtual Environment

Set up a virtual environment to manage dependencies:

```bash
python3 -m venv chatbot
source chatbot/bin/activate  # On Linux/macOS
chatbot\Scripts\activate    # On Windows
```

## 5. Install Required Packages

Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

## 6. Populate the Documentation Chunks

Convert markdown files into vector embeddings and store them in ChromaDB:

```bash
python populate_database.py
```

## 7. Run the Server

Start the Flask server:

```bash
python server.py
```

## 8. Run the Chatbot

Open `chatbot.html` in a web browser to interact with the chatbot.

---

### Troubleshooting
- If you encounter a missing module error, reinstall dependencies:  
  ```bash
  pip install -r requirements.txt
  ```
- Ensure Ollama is installed and running properly.
- If changes are made to the documentation, rerun `populate_database.py`.

Let me know if you need further assistance! 🚀

