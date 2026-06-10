from dotenv import load_dotenv

from app.utils.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store,
)

load_dotenv()

text = (
    """
National Education Policy promotes
skill development and innovation.
"""
    * 200
)

vector_store = create_vector_store(text)

save_vector_store(vector_store)

print("Saved Successfully")

loaded_store = load_vector_store()

print("Loaded Successfully")
print("Total vectors:", loaded_store.index.ntotal)
