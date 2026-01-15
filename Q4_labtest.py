import streamlit as st
import nltk
from PyPDF2 import PdfReader

nltk.download("punkt")
nltk.download("punkt_tab")

# -----------------------------
# Web App Configuration
# -----------------------------
st.set_page_config(page_title="PDF Sentence Chunking (NLTK)", layout="wide")
st.title("Text Chunking Web App using NLTK Sentence Tokenizer")

st.write(
    "This application uploads a PDF file, extracts its text, "
    "and performs sentence-based semantic chunking using NLTK."
)

# -----------------------------
# Step 1: Upload PDF
# -----------------------------
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    try:
        # Read PDF using PdfReader
        reader = PdfReader(uploaded_file)

        # Extract text from PDF
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + " "

        st.subheader("Step 2: PDF Text Extraction")
        st.write(f"Total pages: **{len(reader.pages)}**")
        st.write(f"Total characters extracted: **{len(full_text)}**")

        if full_text.strip() == "":
            st.warning("No text could be extracted from the PDF.")
        else:
            # -----------------------------
            # Sentence Tokenization
            # -----------------------------
            sentences = nltk.sent_tokenize(full_text)

            st.subheader("Sample Extracted Sentences (Index 58 to 68)")

            start_index = 58
            end_index = 69 

            if len(sentences) >= end_index:
                for i in range(start_index, end_index):
                    st.markdown(f"**Sentence {i}:** {sentences[i]}")
            else:
                st.warning(
                    "The document does not contain enough sentences "
                    "to display indices 58 to 68."
                )

            # -----------------------------
            # Step 4: Semantic Sentence Chunking
            # -----------------------------
            st.subheader("Step 4: Semantic Sentence Chunking Output")

            chunked_sentences = sentences[start_index:end_index]

            for idx, chunk in enumerate(chunked_sentences, start=start_index):
                st.markdown(f"**Chunk {idx}:** {chunk}")

    except Exception as e:
        st.error(f"Error processing PDF: {e}")

else:
    st.info("Please upload a PDF file to begin.")
