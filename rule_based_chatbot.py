# Rule-Based Chatbot using if-elif-else
print("🤖 Hello! I am ChatBot. Type 'exit' to end the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello there! How can I help you today?")
    elif user_input == "how are you":
        print("Bot: I'm just a bunch of code, but I'm doing great! 😊")
    elif user_input == "what is your name":
        print("Bot: I am a simple rule-based chatbot created using Python.")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day! 👋")
        break
    elif user_input == "help":
        print("Bot: You can ask me things like 'hello', 'how are you', 'what is your name', or type 'bye' to exit.")
    elif user_input == "exit":
        print("Bot: Exiting the chat. See you next time!")
        break
    else:
        print("Bot: I'm sorry, I didn't understand that. Can you try something else?")
