
# Basic AI Agent
# --------------------------------------------------

from langchain_ollama import OllamaLLM
# Load AI Model Mistral
llm = OllamaLLM(model="mistral")
print("Mistral AI Agent is ready.")

while True:
    question = input(" Type your question or 'exit' to quit : ")
    if question.strip().lower() == "exit":
        print("Exiting agent.")
        break
    response = llm.invoke(question)
    print("Agent:", response)
