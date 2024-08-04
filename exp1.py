def simple_chatbot(user_input):
    responses={
        "hi":"Hello! How can i help you today?",
        "how are you":"I'm just a computer program but thanks for asking.",
        "favorite color":"I dont have a favorite color, but I like the sound of hexadecimal"
    }
    user_input_lower=user_input.lower()
    if user_input_lower in responses:
        return responses[user_input_lower]
    else:
        return "Im sorry I cant answer that"
    
def main():
    print("Hello! Im a simple chatbot. How can I help you?")
    while True:
        user_input=input("User: ")
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day")
            break
        else:
            response=simple_chatbot(user_input)
            print("Chatbot: ",response)

if __name__ == "__main__":
    main()
