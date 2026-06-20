import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_policy_summary(text):

    prompt = f"""
    You are an expert policy analyst.

    Analyze the policy document and provide the response in the following format:

    # Executive Summary

    # Eligibility Criteria

    # Benefits

    # Restrictions

    # Important Dates

    # Key Recommendations

    Policy Document:

    {text[:15000]}
    """

    response = model.generate_content(prompt)

    return response.text


def generate_policy_recommendations(category, document_text):

    prompt = f"""
   You are an expert government policy advisor.

   Category:
   {category}

   Based on the document, recommend exactly 3 related
   government policies or initiatives.

   Return your answer in this format:

   # Recommendation 1
   Policy Name:
   Reason:

   # Recommendation 2
   Policy Name:
   Reason:

   # Recommendation 3
   Policy Name:
   Reason:

   Document:

   {document_text[:3000]}
   """

    response = model.generate_content(prompt)

    return response.text


def generate_response(prompt):

    response = model.generate_content(prompt)

    return response.text


def generate_policy_analysis(document_text):

    prompt = f"""
    You are an expert policy analyst.

    Analyze the document and provide:

    # Benefits

    # Risks

    # Challenges

    # Suggestions

    Document:

    {document_text[:4000]}
    """

    response = model.generate_content(prompt)

    return response.text
