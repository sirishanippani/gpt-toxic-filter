import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# Load OpenAI API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to classify comment using GPT
def classify_comment(comment):
    prompt = f"""
You are a moderation assistant. Classify the following comment as:
1. Non-toxic
2. Mildly toxic
3. Highly toxic

Comment: "{comment}"

Return only the label (1, 2, or 3).
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="GPT Toxic Comment Filter", page_icon="🚨")
st.title("🧼 GPT Toxic Comment Filter")
st.write("Enter a comment below to check for toxicity using GPT.")

user_input = st.text_area("💬 Your Comment:")

if st.button("Classify Comment"):
    if user_input.strip():
        label = classify_comment(user_input)
        if label == "1":
            st.success("✅ Non-toxic")
        elif label == "2":
            st.warning("⚠️ Mildly toxic")
        elif label == "3":
            st.error("❌ Highly toxic")
        else:
            st.info(f"🤔 Unclear response: {label}")
    else:
        st.warning("Please enter a comment before submitting.")