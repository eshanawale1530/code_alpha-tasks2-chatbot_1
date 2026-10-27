
# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I'm ChatBot, your virtual assistant!"

    elif user_input == "help":
        return "Sure! How can I help you?"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."

# Main program
print("===== Welcome to ChatBot =====")
print("Type 'hello', 'how are you', 'help', or 'bye'.")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower().strip() == "bye":
        break

print("Chatbot session ended.")
