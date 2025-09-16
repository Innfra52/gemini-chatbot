import openai

# Replace with your actual API key
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# The rest of your code goes here
# ...

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def chat_with_gpt(prompt):
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    response = chat_with_gpt(user_input)
    print(f"Bot: {response}")