import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load vectorizer
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Title
st.title("📰 Fake News Detection System")

st.write("Check whether news is REAL or FAKE")

# User input
news = st.text_area("Enter News Text")

# Predict button
if st.button("Check News"):

    if news.strip() == "":
        st.warning("Please enter news text")

    else:

        # Convert text
        transformed_news = vectorizer.transform([news])

        # Prediction
        prediction = model.predict(transformed_news)

        # Result
        if prediction[0] == 1:
            st.success("✅ REAL NEWS")

        else:
            st.error("❌ FAKE NEWS")