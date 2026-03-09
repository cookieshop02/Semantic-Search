import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Semantic Search App")

question = st.text_input("Ask a question:")

if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            response = requests.post(
                f"{API_URL}/ask",
                params={"question": question}  # FastAPI reads `str` params as query params
            )
            if response.status_code == 200:
                st.write("**Answer:**", response.json()["answer"])
            else:
                st.error(f"Error: {response.status_code}")
    else:
        st.warning("Please enter a question.")