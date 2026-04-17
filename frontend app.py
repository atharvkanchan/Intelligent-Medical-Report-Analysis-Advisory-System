import streamlit as st
import requests

st.title("🏥 AI Medical Report Analyzer")

uploaded_file = st.file_uploader("Upload Medical Report (PDF)")

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:8000/analyze", files=files)
    data = response.json()

    st.subheader("📄 Summary")
    st.write(data["summary"])

    st.subheader("⚠️ Risks")
    st.write(data["risks"])

    question = st.text_input("Ask question about report")

    if st.button("Ask"):
        res = requests.post(
            "http://127.0.0.1:8000/ask",
            params={"question": question, "context": data["text"]}
        )
        st.write(res.json())
