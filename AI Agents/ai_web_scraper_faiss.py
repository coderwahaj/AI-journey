# Import chat message history from LangChain
from langchain_community.chat_message_histories import ChatMessageHistory
# Import prompt template from LangChain
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM  # Import Ollama LLM integration
import streamlit as st  # Import Streamlit for UI
import requests  # Import requests for HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
import faiss
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import document
import numpy as np

# Initialize the Ollama LLM with the "mistral" model
llm = OllamaLLM(model="mistral")

# Initialize HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize FAISS index and vector store
index = faiss.IndexFlatL2(384)
vector_store = {}

def scrap_website(url):
    """
    Scrapes the website for paragraph text and returns the first 5000 characters.
    Handles errors gracefully.
    """
    try:
        # Show scraping status with emoji
        st.write(f"🌐 Scraping website: **{url}** ...")
        headers = {"User-Agent": "Mozilla/5.0"}  # Set user agent header
        response = requests.get(url, headers=headers, timeout=10)  # Make HTTP request

        if response.status_code != 200:
            # Show error if status not OK
            st.error(f"🚨 Failed to fetch website! Status code: {response.status_code}")
            return None
        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")  # Find all paragraph tags
        # Extract text from paragraphs
        text = " ".join([p.get_text() for p in paragraphs])
        if not text.strip():
            # Warn if no content found
            st.warning("⚠️ No paragraph content found on the page.")
            return None
        # Show success message with emoji
        st.success("✅ Website scraped successfully!")
        return text[:5000]  # Return first 5000 characters of text
    except requests.exceptions.RequestException as e:
        # Handle network errors with emoji
        st.error(f"🚨 Network error: {e}")
        return None
    except Exception as e:
        # Handle other errors with emoji
        st.error(f"🚨 An error occurred while scraping the website: {e}")
        return None

def store_in_faiss(text, url):
    """
    Stores the scraped text in the FAISS vector store.
    """
    global index, vector_store
    # Show storing status with emoji
    st.write("💾 Storing data in FAISS...")

    # Split text into chunks for embedding
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = splitter.split_text(text)

    # Generate embeddings for each chunk
    vectors = embeddings.embed_documents(texts)
    vectors = np.array(vectors, dtype=np.float32)

    # Add vectors to FAISS index
    index.add(vectors)
    # Store url and text in vector_store dictionary
    vector_store[len(vector_store)] = (url, text)
    # Show success message with emoji
    st.success("✅ Data stored successfully in FAISS!")
    return "Data stored Successfully"

def retrieve_answer(query):
    """
    Retrieves an answer to the user's query based on stored content.
    """
    global index, vector_store
    # Embed the query
    query_vector = np.array(embeddings.embed_query(query), dtype=np.float32).reshape(1, -1)

    # Search for similar vectors in FAISS
    D, I = index.search(query_vector, k=2)
    context = ""
    for idx in I[0]:
        if idx in vector_store:
            context += " ".join(vector_store[idx][1]) + "\n\n"
    if not context:
        # Show warning if no relevant data found
        st.warning("🤔 No relevant data found for your question.")
        return "No relevant Data found."

    # Use LLM to generate answer based on context
    answer = llm.invoke(
        f"Based on the following context, answer the question:\n\n{context}\n\nQuestion: {query}"
    )
    return answer

def summarize_content(content):
    """
    Summarizes the provided content using the LLM.
    """
    try:
        # Show summarization status with emoji
        st.write("📝 Summarizing content...")
        # Call LLM to summarize
        summary = llm.invoke(
            f"Summarize the following content:\n\n{content[:1000]}"
        )
        # Show success message with emoji
        st.success("🎉 Content summarized!")
        return summary
    except Exception as e:
        # Handle errors with emoji
        st.error(f"🚨 Error during summarization: {e}")
        return "Could not summarize content."

# Streamlit UI

# Set app title with emoji
st.title("🌟 AI Powered Web Scraper & Summarizer with FAISS Storage")
# App description with emoji
st.write("🔗 Enter a website URL and store its knowledge for AI-based Q&A! ✨")

# Input field for URL with emoji
url = st.text_input("🔎 Enter a website URL")
if url:
    content = scrap_website(url)  # Scrape website content
    if content:
        # Store content in FAISS and show status
        store_message = store_in_faiss(content, url)
        st.write(f"💾 {store_message}")
        # Summarize content and display
        summary = summarize_content(content)
        st.subheader("📋 Summary")
        st.write(summary)
    else:
        st.warning("⚠️ Unable to process the provided URL.")

# Input field for user query with emoji
query = st.text_input("❓ Ask a question based on stored content")
if query:
    answer = retrieve_answer(query)
    st.subheader("🤖 AI Answer:")
    st.write(answer)
