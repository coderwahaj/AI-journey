from langchain_ollama import OllamaLLM
import speech_recognition as sr
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
import pyttsx3

llm = OllamaLLM(model="mistral")

chat_history = ChatMessageHistory()

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
        print("🎤 Listening...")
        recoginzer.adjust_for_ambient_noise(source)
        audio = recoginzer.listen(source)
    try:
        query = recoginzer.recognize_google(audio)
        print(f"🗣️ You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("❓ I could not understand. Please try again.")
        return ""
    except sr.RequestError:
        print("⚠️ Google Speech Recognition service not found.")
        return ""

prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous Conversation: {chat_history}\nUser: {question}\nAI:"
)

def run_chain(question):
    """Generate a response from the LLM and update chat history."""
    # Format chat history as a string for the prompt
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])
    # Generate a response from the LLM using the formatted prompt
    response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))
    # Add the user's question and AI's response to the chat history
    chat_history.add_user_message(question)
    chat_history.add_ai_message(response)
    return response

# Greet the user
speak("Hello! I am your AI Assistant. How can I help you? 🤖")
while True:
    query = listen()
    # Check for exit commands
    if query.strip().lower() == "exit" or query.strip().lower() == "stop":
        speak("👋 Exiting agent. Goodbye!")
        break
    ai_response = run_chain(query)
    print(f"🤖 AI: {ai_response}")
    speak(ai_response)
