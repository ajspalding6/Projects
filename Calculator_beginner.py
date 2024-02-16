import time
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def operationInput():

    invalidSelection = True

    while invalidSelection:

        action = input("Please select which arithmatic operation to execute: \na) Add \nb) Subtract\nc) Multiply\nd) Divide\n> ")
        action_lower = action.lower()

        invalidSelection = False

        if action_lower == 'a':
            print(f"Result: {add(num1, num2)}")
        elif action_lower == 'b':
            print(f"Result: {subtract(num1, num2)}")
        elif action_lower == 'c':
            print(f"Result: {multiply(num1, num2)}")
        elif action_lower == 'd':
            print(f"Result: {divide(num1, num2)}")
        else:
            invalidSelection = True

    return invalidSelection, action_lower

validNum = False

while not validNum:
    num1 = input("Please enter a number: ")
    num2 = input("Please enter a second numner: ")
    try:
        num1 = float(num1) 
        num2 = float(num2)
        validNum = True
    except ValueError:
        print("Please enter valid numbers")
        time.sleep(2)

action = input("Please select which arithmatic operation to execute: \na) Add \nb) Subtract\nc) Multiply\nd) Divide\n> ")
action_lower = action.lower()


if action_lower == 'a':
    print(f"Result: {add(num1, num2)}")
elif action_lower == 'b':
    print(f"Result: {subtract(num1, num2)}")
elif action_lower == 'c':
    print(f"Result: {multiply(num1, num2)}")
elif action_lower == 'd':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid selection")
    time.sleep(2)
    operationInput()





    
