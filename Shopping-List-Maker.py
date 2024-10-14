# Task 1: Write a function that lets the user add items to a list.

# Task 2: Include a function to remove items from the list.

# Task 3: Add a function that prints out the entire list in a formatted way.

current_list = []
print("Welcome to Your Shopping List!")

def shopping_list():
    while True:
        print("\n=== Main Menu ===")
        print("1. Add Item\n2. Remove Item\n3. Check List\n4. Quit")
        user_choice = int(input("Enter number selection: "))
        
        if user_choice == 1:
            add()
        elif user_choice == 2:
            remove()
        elif user_choice == 3:
            check()
        elif user_choice == 4:
            print("Thanks for using the Shopping List App!\nGoodbye!")
            break
        else:
            print("Invalid Entry, try again.")

def add():
    add_to_list = input("Enter Item to Add: ").lower()
    current_list.append(add_to_list)
    print(f"{add_to_list} added to list.")

def remove():
    remove_from_list = input("Enter Item to Remove: ").lower()
    if remove_from_list in current_list:
        current_list.remove(remove_from_list)
        # I previously used .pop() however that caused errors due to it looking to remove the last index item. I switched to .remove() which takes all data values.
        print(f"{remove_from_list} removed from list.")
    else:
        print(f"{remove_from_list} is not in the list.")

def check():
    if not current_list:
        print("Your shopping list is empty.")
    else:
        print("===Current List===:")
        for item in current_list:
            print(f"\{item}")

shopping_list()
