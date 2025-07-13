import streamlit as st
from langchain_ollama import OllamaLLM
import speech_recognition as sr
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
import pyttsx3

llm = OllamaLLM(model="mistral")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()

engine = pyttsx3.init()
engine.setProperty("rate", 160)

recoginzer = sr.Recognizer()

def speak(text):
    """Speak the given text using text-to-speech engine."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice and convert it to text."""
    with sr.Microphone() as source:
        st.write("🎤 Listening...")
        recoginzer.adjust_for_ambient_noise(source)
        audio = recoginzer.listen(source)
    try:
        query = recoginzer.recognize_google(audio)
        st.write(f"🗣️ You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        st.write("❓ I could not understand. Please try again.")
        return ""
    except sr.RequestError:
        st.write("⚠️ Google Speech Recognition service not found.")
        return ""

prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous Conversation: {chat_history}\nUser: {question}\nAI:"
)

def run_chain(question):
    """Generate a response from the LLM and update chat history."""
    # Format chat history as a string for the prompt
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])
    response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))
    # Add the user's question and AI's response to the chat history
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)
    return response

# Set the title of the Streamlit app with an emoji
st.title("🤖 AI Voice Assitant chatBot")
# Display a short description with an emoji
st.write("💬 Click the button below to Ask me Anything!")


# Add a "Start Listening" button for voice input
if st.button("🎤 Start Listening"):
    voice_query = listen()
    if voice_query:
        response = run_chain(voice_query)
        st.write(f"🧑 User: {voice_query}")
        st.write(f"🤖 AI: {response}")
        speak(response)


# Display the chat history with a subheader and emoji
st.subheader("📜 Chat History")
for msg in st.session_state.chat_history.messages:
    # Show each message with the sender type and content
    st.write(f"{msg.type.capitalize()}: {msg.content}")
