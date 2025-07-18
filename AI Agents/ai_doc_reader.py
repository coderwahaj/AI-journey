# 🌟 AI Powered Document Reader & ChatBot

import streamlit as st  # Streamlit for UI
import PyPDF2  # PDF reading
import numpy as np
import time

from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
import faiss

# --- Model & Embeddings Initialization ---
llm = OllamaLLM(model="mistral")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# --- FAISS Index & Store ---
index = faiss.IndexFlatL2(384)
vector_store = {}

# --- PDF Extraction ---
def extract_text_from_pdf(upload_file):
    """Extracts all text from a PDF file."""
    pdf_reader = PyPDF2.PdfReader(upload_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# --- Store Text in FAISS ---
def store_in_faiss(text, filename):
    """
    Stores the text chunks and their embeddings in the FAISS vector store.
    """
    global index, vector_store
    st.info(f"💾 Storing document: {filename} ...")

    # Split text into manageable chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = splitter.split_text(text)

    # Generate embeddings for each chunk
    vectors = np.array(embeddings.embed_documents(texts), dtype=np.float32)
    index.add(vectors)

    # Store filename and text in vector_store
    for i, chunk in enumerate(texts):
        vector_store[len(vector_store)] = (filename, chunk)

    st.success("✅ Document stored successfully in FAISS!")
    return "Data stored successfully."

# --- Retrieve Answer from Stored Content ---
def retrieve_answer(query):
    """
    Retrieves an answer to the user's query based on stored document content.
    """
    global index, vector_store
    query_vector = np.array(embeddings.embed_query(query), dtype=np.float32).reshape(1, -1)
    D, I = index.search(query_vector, k=2)

    context = ""
    for idx in I[0]:
        if idx in vector_store:
            context += vector_store[idx][1] + "\n\n"

    if not context:
        st.warning("🤔 No relevant data found for your question.")
        return "No relevant data found."

    st.info("🤖 Generating answer ...")
    start = time.time()
    answer = llm.invoke(
        f"Based on the following context, answer the question:\n\n{context}\n\nQuestion: {query}"
    )
    end = time.time()
    st.write(f"⏱️ Time taken: {end - start:.2f} seconds")
    return answer

# --- Summarize Content ---
def summarize_content(content):
    """
    Summarizes the provided content using the LLM.
    """
    try:
        st.info("📝 Summarizing content ...")
        summary = llm.invoke(f"Summarize the following content:\n\n{content[:1000]}")
        st.success("🎉 Content summarized!")
        return summary
    except Exception as e:
        st.error(f"🚨 Error during summarization: {e}")
        return "Could not summarize content."

# --- Streamlit UI ---
st.set_page_config(page_title="AI Doc Reader", page_icon="🌟")
st.title("🌟 AI Powered Document Reader & ChatBot")
st.write("🔗 Upload a PDF and store its knowledge for AI-based Q&A! ✨")

uploaded_file = st.file_uploader("📄 Upload a PDF Document", type=["pdf"])
if uploaded_file:
    with st.spinner("📖 Extracting text from PDF..."):
        content = extract_text_from_pdf(uploaded_file)
    store_message = store_in_faiss(content, uploaded_file.name)
    st.info(store_message)

    # Option to summarize the document
    if st.button("📝 Summarize Document"):
        summary = summarize_content(content)
        st.subheader("📃 Document Summary")
        st.write(summary)

query = st.text_input("❓ Ask a question based on stored document content")
if query:
    answer = retrieve_answer(query)
    st.subheader("🤖 AI Answer:")
    st.write(answer)
