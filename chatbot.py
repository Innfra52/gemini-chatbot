while True:
    user_input = input("You: ")

    if user_input.lower() == "hello":
        print("Bot: Hi there! How can I help you today?")
    elif "how are you" in user_input.lower():
        print("Bot: I'm a bot, but I'm doing great! Thanks for asking.")
    elif "bye" in user_input.lower():
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: I'm sorry, I don't understand that yet.")