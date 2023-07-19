def greet():
    print("Hello! How can I assist you today?")

def process_user_input(user_input):
    if user_input.lower() == "hello":
        print("Hi there!")
    elif user_input.lower() == "how are you?":
        print("I'm doing well, thank you!")
    elif user_input.lower() == "goodbye":
        print("Goodbye! Have a great day!")
        return True  # Exit the main loop

def main():
    greet()
    while True:
        user_input = input("> ")
        if process_user_input(user_input):
            break  # Exit the main loop

if __name__ == "__main__":
    main()
