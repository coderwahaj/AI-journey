# Import chat message history from LangChain
from langchain_community.chat_message_histories import ChatMessageHistory
# Import prompt template from LangChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM  # Import Ollama LLM integration
import streamlit as st  # Import Streamlit for UI
import requests  # Import requests for HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing

# Initialize the Ollama LLM with the "mistral" model
llm = OllamaLLM(model="mistral")


def scrap_website(url):
    """
    Scrapes the website for paragraph text and returns the first 2000 characters.
    Handles errors gracefully.
    """
    try:
        # Display scraping status
        st.write(f"🌐 Scraping website: **{url}** ...")
        headers = {"User-Agent": "Mozilla/5.0"}  # Set user agent header
        response = requests.get(url, headers=headers,
                                timeout=10)  # Make HTTP request

        if response.status_code != 200:
            # Show error if status not OK
            st.error(
                f"🚨 Failed to fetch website! Status code: {response.status_code}")
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
        st.success("✅ Website scraped successfully!")  # Show success message
        return text[:2000]  # Return first 2000 characters of text
    except requests.exceptions.RequestException as e:
        st.error(f"🚨 Network error: {e}")  # Handle network errors
        return None
    except Exception as e:
        # Handle other errors
        st.error(f"🚨 An error occurred while scraping the website: {e}")
        return None


def summarize_content(content):
    """
    Summarizes the provided content using the LLM.
    """
    try:
        st.write("📝 Summarizing content...")  # Display summarization status
        # Call LLM to summarize
        summary = llm.invoke(
            f"Summarize the following content\n\n{content[:1000]}")
        st.success("🎉 Content summarized!")  # Show success message
        return summary  # Return summary
    except Exception as e:
        st.error(f"🚨 Error during summarization: {e}")  # Handle errors
        return "Could not summarize content."


# Streamlit UI
st.title("🌟AI Web Scraper & Summarizer")  # Set app title
# App description
st.write("🔗 Enter a website URL and get a beautiful summarized version! ✨")

url = st.text_input("🔎 Enter a website URL")  # Input field for URL
if url:
    content = scrap_website(url)  # Scrape website content
    if content:
        st.write(content)
        summary = summarize_content(content)
        # Summarize content
        st.subheader("📋 Summary")  # Display summary header
        st.write(summary)  # Show summary
    else:
        # Warn if unable to process
        st.warning(
            "⚠️ Unable to retrieve or summarize content from the provided URL.")
