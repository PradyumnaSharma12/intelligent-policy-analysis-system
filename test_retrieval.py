from dotenv import load_dotenv

from app.utils.vector_store import retrieve_relevant_chunks

load_dotenv()

query = "What does the National Education Policy promote?"

results = retrieve_relevant_chunks(query)

print(f"Retrieved {len(results)} chunks\n")

for i, doc in enumerate(results, start=1):
    print(f"\nChunk {i}")
    print("-" * 50)
    print(doc.page_content[:500])
