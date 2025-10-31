import streamlit as st
import openai
import os

# Load your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Genius AI", page_icon="🤖")
st.title("🤖 Genius AI")
st.write("Welcome to Genius AI — your smart web assistant!")

# User input
question = st.text_input("Ask me anything:")

if question:
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful and smart AI assistant named Genius AI."},
                    {"role": "user", "content": question}
                ]
            )
            answer = response["choices"][0]["message"]["content"]
            st.write(f"**Answer:** {answer}")
        except Exception as e:
            st.error("Sorry, there was an error. Please try again later.")
