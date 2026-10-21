# Undo and Redo using Two Stacks

text = ""
undo_stack = []
redo_stack = []

while True:
    print("\n--- Text Editor ---")
    print("1. Write text")
    print("2. Undo")
    print("3. Redo")
    print("4. Display text")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        undo_stack.append(text)
        text = input("Enter text: ")
        redo_stack.clear()
        print("Text added successfully!")

    elif choice == "2":
        if undo_stack:
            redo_stack.append(text)
            text = undo_stack.pop()
            print("Undo successful!")
        else:
            print("Nothing to undo!")

    elif choice == "3":
        if redo_stack:
            undo_stack.append(text)
            text = redo_stack.pop()
            print("Redo successful!")
        else:
            print("Nothing to redo!")

    elif choice == "4":
        print("Current text:", text)

    elif choice == "5":
        print("Exiting text editor...")
        break

    else:
        print("Invalid choice!")