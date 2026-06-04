import streamlit as st
import tempfile
from dotenv import load_dotenv

from utils import (
    load_pdf,
    create_vector_store,
    get_qa_chain
)

load_dotenv()

st.set_page_config(
    page_title="PDF Chatbot",
    page_icon="📄"
)

st.title("📄 PDF Chatbot with Groq")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    with st.spinner("Processing PDF..."):
        docs = load_pdf(pdf_path)
        vectorstore = create_vector_store(docs)
        qa_chain = get_qa_chain(vectorstore)

    st.success("PDF loaded successfully!")

    question = st.text_input(
        "Ask a question about the PDF"
    )

    if question:

        with st.spinner("Thinking..."):
            response = qa_chain.run(question)

        st.subheader("Answer")
        st.write(response)
