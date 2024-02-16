import time

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def operation_input():
    invalid_selection = True

    while invalid_selection:
        action = input("Please select which arithmetic operation to execute: \n"
                       "a) Add \n"
                       "b) Subtract\n"
                       "c) Multiply\n"
                       "d) Divide\n"
                       "> ")
        action_lower = action.lower()

        if action_lower == 'a':
            print(f"Result: {add(num1, num2)}")
            invalid_selection = False
        elif action_lower == 'b':
            print(f"Result: {subtract(num1, num2)}")
            invalid_selection = False
        elif action_lower == 'c':
            print(f"Result: {multiply(num1, num2)}")
            invalid_selection = False
        elif action_lower == 'd':
            print(f"Result: {divide(num1, num2)}")
            invalid_selection = False
        else:
            print("Invalid selection")

    return invalid_selection, action_lower

valid_num = False

while not valid_num:
    num1 = input("Please enter a number: ")
    num2 = input("Please enter a second number: ")
    try:
        num1 = float(num1)
        num2 = float(num2)
        valid_num = True
    except ValueError:
        print("Please enter valid numbers")
        time.sleep(2)

operation_input()
