from app.utils.vector_store import chunk_text

sample_text = (
    """
Artificial Intelligence is transforming policy analysis.
"""
    * 500
)

chunks = chunk_text(sample_text)

print(f"Total Chunks: {len(chunks)}")
print(chunks[0][:200])
