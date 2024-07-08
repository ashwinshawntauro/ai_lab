def conversation(user_input):
    response={
        "hi":"Hello how are you?",
        "help me":"How can i help you?",
        "what is your name":"My name is chatbot",
        "who created you":"I was created by AI programmer at openAI"
    }
    user_input_low=user_input.lower()
    if user_input_low in response:
        return response[user_input_low]
    else:
        return "Sorry could not understand"
       


def main():
    print("----AI Chatbot---")
    while True:
        user_input=input("You: ")
        if user_input=="bye":
            print("Thank you hope to see you back!")
            return
        else:
            talk=conversation(user_input)
            print("AI: ",talk)

if __name__ =="__main__":
    main()