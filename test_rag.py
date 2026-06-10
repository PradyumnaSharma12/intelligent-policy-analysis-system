from dotenv import load_dotenv

from app.utils.rag_service import ask_policy

load_dotenv()

question = "What does the National Education Policy promote?"

answer = ask_policy(question)

print(answer)
