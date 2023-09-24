print("Welcome to the ChatBot!")
name = input("What's your name? ")
age = input("How old are you? ")
print(f"Nice to meet you, {name}! How can I assist you today?")
while True:
    print("\nMenu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

    choice = input("Please choose an option (1/2/3/4): ")

    if choice == '1':
        print("You selected Option 1. This is a placeholder.")
    elif choice == '2':
        print("You selected Option 2. This is a placeholder.")
    elif choice == '3':
        print("You selected Option 3. This is a placeholder.")
    elif choice == '4':
        print("Goodbye! Have a great day!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
