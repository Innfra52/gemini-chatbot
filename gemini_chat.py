import google.generativeai as genai
import os

# Put your API key here or, better yet, set it as an environment variable
genai.configure(api_key="AIzaSyBBNX-CD-gH74vEFM2toa1YIDp5w_RFeGg")

# Create a Gemini model instance
model = genai.GenerativeModel('gemini-pro')

# Start a new chat session to maintain conversation history
chat = model.start_chat(history=[])

print("Chatbot is ready. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    try:
        # Send the user's message and get a response
        response = chat.send_message(user_input)
        print(f"Bot: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")