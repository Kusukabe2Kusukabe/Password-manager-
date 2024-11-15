# Create an empty dictionary to store passwords
passwords = {}

# Main loop for user interaction
while True:
    print("\nPassword Manager")
    print("1. Add a password")
    print("2. View a password")
    print("3. Search for a password")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    # Add a password
    if choice == "1":
        website = input("Enter the website name: ")
        password = input("Enter the password: ")
        passwords[website] = password
        print(f"Password for {website} added successfully.")

    # View a password
    elif choice == "2":
        website = input("Enter the website name: ")
        if website in passwords:
            print(f"Password for {website}: {passwords[website]}")
        else:
            print(f"No password found for {website}.")

    # Search for a password
    elif choice == "3":
        website = input("Enter the website name to search: ")
        if website in passwords:
            print(f"Password for {website}: {passwords[website]}")
        else:
            print(f"No password found for {website}.")

    # Exit the program
    elif choice == "4":
        print("Exiting Password Manager.")
        break
    
    # Invalid choice
    else:
        print("Invalid choice. Please try again.")
