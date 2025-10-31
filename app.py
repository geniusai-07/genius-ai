import streamlit as st
from openai import OpenAI
import os

# Load API key from environment
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Genius AI", page_icon="🤖")
st.title("🤖 Genius AI")
st.write("Welcome to Genius AI — your smart web assistant!")

question = st.text_input("Ask me anything:")

if question:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful and smart AI assistant."},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content
            st.write(f"**Answer:** {answer}")
        except Exception as e:
            st.error("Sorry, there was an error. Please try again later.")
