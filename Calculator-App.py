# 1. The Calculator App: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

print("\nWelcome to the Calculator App!\n")
        
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        num1 / num2
        return num1 / num2
    except ZeroDivisionError:
        print("You can't divide by 0, please try again.")

def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
        except ValueError:
            print("Please enter a valid number: ")
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter a valid number: ")
        
        user_choice = int(input("Select the operator:\n1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\nSelection: "))

        if user_choice == 1:
            # I couldn't get the code to run properly because I forgot to define a result variable that calls the operator functions. Added result and now the program works.
            result = addition(num1, num2)
            print(f"\nResult: {result}\n")
        elif user_choice == 2:
            result = subtraction(num1, num2)
            print(f"\nResult: {result}\n")
        elif user_choice == 3:
            result = multiply(num1, num2)
            print(f"\nResult: {result}\n")
        elif user_choice == 4:
            result = divide(num1, num2)
            print(f"\nResult: {result}\n")
        else:
            print("Invalid choice, please try again.")
            continue
            
calculator()