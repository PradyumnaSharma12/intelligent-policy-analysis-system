from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings


VECTOR_DB_PATH = "app/vectorstore"


def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, length_function=len
    )

    return splitter.split_text(text)


def get_embeddings():

    return GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


def create_vector_store(text):

    chunks = chunk_text(text)

    embeddings = get_embeddings()

    vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)

    return vector_store


def save_vector_store(vector_store):

    vector_store.save_local(VECTOR_DB_PATH)


def load_vector_store():

    embeddings = get_embeddings()

    return FAISS.load_local(
        VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True
    )


def retrieve_relevant_chunks(query, k=3):

    vector_store = load_vector_store()

    docs = vector_store.similarity_search(query=query, k=k)

    return docs
