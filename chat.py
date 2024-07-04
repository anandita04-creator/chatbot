import re
import random
import json

# List of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"what is your name?", ["I am a chatbot.", "You can call me ChatBot."]),
    (r"how are you?", ["I'm good, thank you!", "Doing well, thank you!"]),
    (r"quit", ["Bye! Take care."])
]

# Default response for unknown inputs
default_response = "I'm sorry, I don't understand that. Can you teach me the correct response?"

def get_response(user_input):
    for pattern, responses in pairs:
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    return default_response

def learn_response(user_input, correct_response):
    new_pattern = re.escape(user_input)
    pairs.append((new_pattern, [correct_response]))
    with open("pairs.json", "w") as f:
        json.dump(pairs, f)

# Load existing pairs if available
try:
    with open("pairs.json", "r") as f:
        pairs = json.load(f)
except FileNotFoundError:
    pass

# Example usage
user_input = input("You: ")
while user_input.lower() != "quit":
    response = get_response(user_input)
    print(f"ChatBot: {response}")
    if response == default_response:
        correct_response = input("You: ")
        learn_response(user_input, correct_response)
        print("ChatBot: Thank you! I've learned something new.")
    user_input = input("You: ")

print("ChatBot: Bye! Take care.")
