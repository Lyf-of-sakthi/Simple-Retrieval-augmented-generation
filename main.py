from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from User_interface import get_file
from Loaded_LLm import generate_answer

file_path = get_file()
if not file_path:
    print("No file selected")
    exit()

loader = TextLoader(file_path)
doc = loader.load()


splitter = RecursiveCharacterTextSplitter(chunk_size =1000, chunk_overlap = 100)
chunks = splitter.split_documents(doc)

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-l6-v2")

vector_store = FAISS.from_documents(chunks, embedding_model)


while True:
    query = input("Enter your query (or 'exit' to quit): ")
    if query.lower() == 'exit':
        break

    query_embedding = embedding_model.embed_query(query)
    relevant_docs = vector_store.similarity_search_by_vector(query_embedding, top_k=5)
    context = " ".join(doc.page_content for doc in relevant_docs)
    response = generate_answer(context, query)
    print("Answer:", response)



'''from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
ex = "Hi my name is Sakthi"
o = model.encode(ex)
print(o)'''

