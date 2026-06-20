import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load API
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("✍️ AI Content Generator")

st.write("Generate blogs, LinkedIn posts, and Twitter threads using AI")

# Inputs
topic = st.text_input("Enter Topic")

tone = st.selectbox(
    "Select Tone",
    ["Formal", "Casual", "Technical", "Creative"]
)

content_type = st.selectbox(
    "Select Content Type",
    ["Blog Post", "LinkedIn Post", "Twitter Thread"]
)

word_limit = st.slider("Word Limit", 50, 500, 150)

if st.button("Generate Content"):

    if topic == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("Generating content..."):

            prompt = f"""
            Generate a {content_type} on the topic: "{topic}".

            Tone: {tone}
            Word Limit: {word_limit}

            Make it engaging and well-structured.
            """

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            output = response.choices[0].message.content

            st.subheader("Generated Content:")
            st.write(output)
