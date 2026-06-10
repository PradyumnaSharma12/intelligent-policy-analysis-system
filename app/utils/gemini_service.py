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


def generate_response(prompt):

    response = model.generate_content(prompt)

    return response.text
