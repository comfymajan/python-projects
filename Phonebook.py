phone= {
    "Police": "110",
    "Fire department":"125",
    "Emergency": "115"
}
while True:
    print("\n1. Show all contacts")
    print("2. Search contact")
    print("3. Search number")
    print("4. Add contact")
    print("5. Remove contact")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        for name,number in phone.items():
            print(name, ":", number)
    elif choice == 2:
        name = input("Enter the name: ").lower()
        if name in phone:
            print("Phone number " + phone[name])
        else:
            print("Invalid name")
    elif choice == 3:
        number = input("Enter the number: ")
        if number in phone.values():
            for name,num in phone.items():
                print("Phone number: "+ name)
        else:
            print("Invalid number")
    elif choice == 4:
        new_name = input("Enter the new name: ")
        new_number = input("Enter the new number: ")
        if new_name in phone:
            print("Contact with this name exists")
        elif new_number in phone:
            print("Contact with this number exists")
        else:
            phone[new_name] = new_number
            print(" Contact added successfully")
    elif choice == 5:
        name_delete = input("Enter the name of the contact: ")
        if name_delete in phone:
            phone.pop(name_delete)
            print(" Contact removed successfully")
        else:
            print("Name does not exist")
    elif choice == 6:
        break
    else:
        print("Invalid choice")