# chatbot_1
A simple Python-based rule-based chatbot that responds to predefined user messages like “hello,” “how are you,” and “bye.” Built using functions, if-elif-else statements, loops, and basic input/output.
Here’s a GitHub-ready description for your Python Rule-Based Chatbot with its code explanation.

# Python Rule-Based Chatbot 🤖

## Description

A simple rule-based chatbot developed using Python that interacts with users through predefined messages and responses. It responds to inputs such as "hello", "how are you", "help", and "bye".

## Features

- Responds to predefined user messages.
- Accepts case-insensitive input.
- Uses a continuous conversation loop.
- Ends the conversation when the user types "bye".
- Provides a default response for unrecognized messages.

## Technologies Used

- Python
- Functions
- If-elif-else statements
- While loop
- Input and output

## Code Explanation

- `def chatbot_response()` defines a function that processes user input and returns an appropriate response.
- `lower()` converts input to lowercase, making responses case-insensitive.
- `strip()` removes extra spaces from the beginning and end of the input.
- `if-elif-else` checks the user's message against predefined rules.
- `while True` keeps the conversation running until the user exits.
- `input()` accepts messages from the user.
- `print()` displays the chatbot's responses.
- `break` stops the loop when the user types "bye".

## How to Run

1. Install Python on your computer.
2. Clone or download this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

```
python chatbot.py
```

## Learning Outcomes

This project demonstrates the fundamentals of Python functions, conditional statements, loops, string manipulation, and console-based interaction.

**Note:** This is a rule-based chatbot that uses predefined responses rather than artificial intelligence or machine learning.

Suggested repository name: `python-rule-based-chatbot`

code : 


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
