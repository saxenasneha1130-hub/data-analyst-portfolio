def chatbot(user_input):
    user_input = user_input.lower()
    
    if user_input == "hello":
        return "Hi! How are you? 😊"
    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"
    elif user_input == "bye":
        return "Goodbye! Have a great day! 👋"
    elif user_input == "what is your name":
        return "I'm SnehaBot! 🤖"
    elif user_input == "what can you do":
        return "I can chat with you! Try: hello, how are you, bye"
    else:
        return "Sorry, I don't understand that. Try: hello, how are you, bye"

print("🤖 Welcome to SnehaBot!")
print("Type 'bye' to exit\n")

while True:
    user = input("You: ")
    response = chatbot(user)
    print("SnehaBot:", response)
    
    if user.lower() == "bye":
        break