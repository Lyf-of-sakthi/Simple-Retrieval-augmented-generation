# Document-Based Question Answering using Hugging Face

## Overview

This project enables document-based question answering using a transformer model from Hugging Face. The system loads a document, splits it into chunks, embeds the text using a pre-trained model, stores embeddings in a FAISS vector database, and retrieves the most relevant context for answering user queries.

## Features

- Uses `tiiuae/falcon-7b-instruct` for generating responses.
- Loads and processes text documents.
- Embeds document content using `all-MiniLM-l6-v2`.
- Stores and retrieves relevant document chunks with FAISS.
- Provides an interactive query system.

## Requirements

Ensure the following dependencies are installed:

```bash
pip install huggingface_hub transformers langchain langchain-community langchain-huggingface sentence-transformers faiss-cpu tkinter
```

## Project Structure

```
|-- project_directory/
    |-- main.py               # Main script to run the system
    |-- User_interface.py      # Handles file selection
    |-- Loaded_LLm.py          # Manages response generation
    |-- requirements.txt       # List of dependencies
    |-- README.md              # Project documentation
```

## Usage

1. **Set up Hugging Face Token**

   - Replace `token="Upload you huggingface token here"` with your Hugging Face API token.

2. **Run the script**

   ```bash
   python main.py
   ```

3. **Select a document**

   - A file dialog will appear for you to select a text document.

4. **Query the document**

   - Enter questions based on the uploaded document.
   - Type `exit` to stop the program.

## License

This project is open-source and can be modified or distributed under the MIT License.

