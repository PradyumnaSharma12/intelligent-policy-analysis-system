# Intelligent AI-Based Policy Analysis and Recommendation System

## Overview

The Intelligent AI-Based Policy Analysis and Recommendation System is an AI-powered platform designed to automate policy document analysis using Natural Language Processing (NLP), Machine Learning, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs).

The system enables users to upload policy documents in PDF format, automatically classify them into categories, generate executive summaries, perform policy analysis, provide AI-powered recommendations, and interact with the uploaded policy through a question-answering interface.

---

## Features

### Policy Upload and Processing

* Upload policy documents in PDF format
* Automatic text extraction using PyPDF
* Document indexing for retrieval

### Policy Classification

* Machine Learning-based document classification
* TF-IDF Vectorization
* Support Vector Machine (SVM) classifier
* Automatic category prediction

### Policy Summarization

* Executive summary generation
* Key policy insights extraction
* Structured summary output

### AI-Based Recommendations

* Policy improvement suggestions
* Actionable recommendations
* AI-generated strategic insights

### Policy Analysis

* Benefits identification
* Risk assessment
* Challenges detection
* Improvement suggestions

### Retrieval-Augmented Generation (RAG)

* FAISS vector database
* Semantic search
* Context-aware question answering

### Interactive Dashboard

* React + Tailwind frontend
* FastAPI backend
* Real-time AI-powered interactions

---

## System Architecture

PDF Upload
↓
Text Extraction
↓
Policy Classification (ML)
↓
Vector Embedding Generation
↓
FAISS Vector Storage
↓
Policy Analysis & Recommendations
↓
RAG Question Answering
↓
React Dashboard

---

## Tech Stack

### Frontend

* React
* Vite
* Tailwind CSS

### Backend

* FastAPI
* Python 3.12

### AI & NLP

* Google Gemini API
* LangChain
* Retrieval-Augmented Generation (RAG)

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Support Vector Machine (SVM)
* Naive Bayes
* Random Forest

### Vector Database

* FAISS

### Data Processing

* PyPDF

---

## Machine Learning Results

| Model         | Accuracy |
| ------------- | -------- |
| Naive Bayes   | 87%      |
| Random Forest | 80%      |
| SVM           | 86%      |

---

## Project Structure

```text
intelligent-policy-analysis-system/
│
├── api/
│   └── main.py
│
├── app/
│   ├── uploads/
│   ├── vectorstore/
│   ├── models/
│   └── utils/
│
├── frontend/
│
├── datasets/
│
├── docs/
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/PradyumnaSharma12/intelligent-policy-analysis-system.git
cd intelligent-policy-analysis-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn api.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## API Endpoints

### Upload Policy

```http
POST /upload-policy
```

### Summarize Policy

```http
POST /summarize-policy
```

### Ask Questions

```http
POST /ask-policy
```

---

## Future Enhancements

* Multi-document analysis
* Policy comparison engine
* Advanced analytics dashboard
* Cloud deployment
* User authentication
* Policy version tracking

---

## Conclusion

This project demonstrates the integration of Machine Learning, Large Language Models, Retrieval-Augmented Generation, and modern web technologies to create an intelligent platform for automated policy analysis and recommendation generation. The system significantly reduces manual effort while improving the accessibility and understanding of complex policy documents.
