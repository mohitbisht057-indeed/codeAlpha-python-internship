def chatbot():
    print("=== BASIC CHATBOT ===")
    print("Type 'goodbye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi there!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a Python chatbot.")

        elif user == "goodbye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()