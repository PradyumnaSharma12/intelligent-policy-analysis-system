import joblib

classifier = joblib.load("app/models/policy_classifier.pkl")

vectorizer = joblib.load("app/models/tfidf_vectorizer.pkl")

categories = ["Computer Graphics", "Medical", "Politics", "Space"]


def classify_text(text):

    prediction = classifier.predict(vectorizer.transform([text]))

    category = categories[prediction[0]]

    return category
