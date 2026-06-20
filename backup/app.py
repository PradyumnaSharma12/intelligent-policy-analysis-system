import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Policy Analysis System", page_icon="📄", layout="wide")

st.title("📄 Intelligent AI-Based Policy Analysis System")

uploaded_file = st.file_uploader("Upload Policy PDF", type=["pdf"])

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Generate Summary"):
            with st.spinner("Generating summary..."):
                response = requests.post(f"{API_URL}/summarize-policy", files=files)

                if response.status_code == 200:
                    data = response.json()

                    st.subheader("Policy Summary")

                    st.write(data["summary"])

                else:
                    st.error("Failed to generate summary")

    with col2:
        if st.button("Index Policy"):
            with st.spinner("Analyzing policy..."):
                response = requests.post(f"{API_URL}/upload-policy", files=files)

                if response.status_code == 200:
                    data = response.json()

                    st.success("Policy indexed successfully!")

                    st.subheader("🏷 Predicted Category")

                    st.info(data["predicted_category"])

                    st.subheader("🤖 AI Recommendations")

                    st.write(data["ai_recommendations"])

                    st.subheader("📊 Policy Analysis")

                    st.write(data["policy_analysis"])

                else:
                    st.error("Failed to index policy")

st.divider()

st.subheader("Ask Questions About Policy")

question = st.text_input("Enter your question")

if st.button("Ask Policy"):
    if question:
        with st.spinner("Searching policy..."):
            response = requests.post(
                f"{API_URL}/ask-policy", json={"question": question}
            )

            if response.status_code == 200:
                answer = response.json()["answer"]

                st.subheader("Answer")

                st.write(answer)

            else:
                st.error("Error generating answer")
