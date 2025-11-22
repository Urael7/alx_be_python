def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice_input = input("Enter your choice (number): ").strip()

        # Validate that choice_input is an integer
        try:
            choice = int(choice_input)
        except ValueError:
            print("Invalid input. Please enter a number corresponding to a menu option.\n")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' added to the shopping list.\n")

        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the shopping list.\n")
            else:
                print(f"'{item}' not found in the shopping list.\n")

        elif choice == 3:
            if not shopping_list:
                print("The shopping list is empty.\n")
            else:
                print("Current Shopping List:")
                for entry in shopping_list:
                    print(f"- {entry}")
                print()

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.\n")

if __name__ == "__main__":
    main()
