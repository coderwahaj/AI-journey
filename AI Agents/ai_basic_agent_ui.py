# Basic AI Agent with Web Interface
# -------------------------------------
# Import necessary modules for chat history, prompt templates, and the Ollama LLM
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
import streamlit as st

# Initialize the Ollama LLM with the "mistral" model
llm = OllamaLLM(model="mistral")

# Create a chat history object to store conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()

# Define a prompt template that includes previous conversation and the user's question
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous Conversation : {chat_history}\nUser : {question}\nAI :"
)


def run_chain(question):
    # Format chat history as a string for the prompt
    chat_history_text = "\n".join(
        [f"{msg.type.capitalize()}:{msg.content}" for msg in st.session_state.chat_history.messages])
    # Generate a response from the LLM using the formatted prompt
    response = llm.invoke(prompt.format(
        chat_history=chat_history_text, question=question))
    # Add the user's question and AI's response to the chat history
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)
    return response


# Set the title of the Streamlit app with an emoji
st.title("🤖 AI chatBot")
# Display a short description with an emoji
st.write("💬 Ask me Anything!")

# Input box for the user's question
user_input = st.text_input("Your Question:")

# If the user has entered a question, process it
if user_input:
    response = run_chain(user_input)
    # Display the user's question and AI's response
    st.write(f"🧑 User: {user_input}")
    st.write(f"🤖 AI: {response}")

# Display the chat history with a subheader and emoji
st.subheader("📜 Chat History")
for msg in st.session_state.chat_history.messages:
    # Show each message with the sender type and content
    st.write(f"{msg.type.capitalize()}: {msg.content}")

# Basic AI Agent with Memory
# -------------------------------------
# # Import necessary modules for chat history, prompt templates, and the Ollama LLM
# from langchain_community.chat_message_histories import ChatMessageHistory
# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import OllamaLLM

# # Initialize the Ollama LLM with the "mistral" model
# llm = OllamaLLM(model="mistral")

# # Create a chat history object to store conversation history
# chat_history = ChatMessageHistory()

# # Define a prompt template that includes previous conversation and the user's question
# prompt = PromptTemplate(
#     input_variables=["chat_history", "question"],
#     template="Previous Converstion : {chat_history}\nUser : {question}\nAI :"
# )

# def run_chain(question):
#     # Format chat history as a string for the prompt
#     chat_history_text = "\n".join([f"{msg.type.capitalize()}:{msg.content}" for msg in chat_history.messages])
#     # Generate a response from the LLM using the formatted prompt
#     response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))
#     # Add the user's question and AI's response to the chat history
#     chat_history.add_user_message(question)
#     chat_history.add_ai_message(response)
#     return response

# print("Mistral AI Model with Memory is ready.")

# # Main loop to interact with the user
# while True:
#     question = input(" Type your question or 'exit' to quit : ")
#     if question.strip().lower() == "exit":
#         print("Exiting agent.")
#         break
#     ai_response = run_chain(question)
#     print("AI :", ai_response)
