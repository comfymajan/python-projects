shopping_list = []
while True:
    print("\n1. Add item")
    print("2. Show list")
    print("3. Remove item")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print("Item added")
    elif choice == "2":
        for item in shopping_list:
            print(item)
    elif choice == "3":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("Item removed")
        else:
            print("Item not in list")
    elif choice == "4":
        break
    else:
        print("Invalid choice")