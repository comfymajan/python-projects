users = {}
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter an option: ")
    if choice == "1":
        username = input("Enter your username: ")
        if username in users:
            print("Username already exists")
        else:
            password = input("Enter your password: ")
            users[username] = password
            print("User created successfully")
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in users:
            if users.get(username) == password:
                print("Login successful")
            else:
                print("Invalid password")
        else:
            print("Invalid username")
    elif choice == "3":
        break
    else:
        print("Invalid option")