from app.utils.vector_store import retrieve_relevant_chunks
from app.utils.gemini_service import generate_response


def ask_policy(question):

    docs = retrieve_relevant_chunks(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI Policy Analysis Assistant.

Use ONLY the policy context below.

If the answer is not available in the policy,
reply exactly:

"I could not find this information in the uploaded policy."

Policy Context:
{context}

Question:
{question}

Answer:
"""

    answer = generate_response(prompt)

    return answer
