import streamlit as st

st.set_page_config(page_title="Genius AI", page_icon="🤖")

st.title("🤖 Genius AI")
st.write("Welcome to Genius AI — your smart web assistant!")

question = st.text_input("Ask me anything:")

if question:
    st.write(f"You asked: **{question}**")
    st.write("✨ (Here’s where you can connect your AI logic later!)")
