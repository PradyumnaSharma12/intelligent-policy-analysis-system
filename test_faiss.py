from dotenv import load_dotenv
from app.utils.vector_store import create_vector_store

load_dotenv()

sample_text = (
    """
India's National Education Policy focuses on
skill development, digital learning and
multidisciplinary education.
"""
    * 200
)

vector_store = create_vector_store(sample_text)

print("FAISS index created successfully")
print(vector_store.index.ntotal)
