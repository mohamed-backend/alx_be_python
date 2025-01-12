
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []  # Initialize an empty list for shopping items

    while True:
        display_menu()  # Show menu to the user
        choice = input("Enter your choice: ")  # Get the user's choice

        if choice == '1':
            # Prompt user to add an item (updated prompt to match the required format)
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # Add the item to the list
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == '2':
            # Prompt user to remove an item
            item = input("Enter the name of the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item from the list
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")
        
        elif choice == '3':
         
            if shopping_list:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")  # Display items in the list with index
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':
        
            print("Goodbye!")
            break  
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()





