name = input("Please enter your name: ")
validName = False
while not validName:
    try:
        name = float(name)
        name = input("Please enter a valid name: ")
    except ValueError:
        validName = True
        pass
    
age = input("Please enter your age: ")
futureAge = float(age) + 5
print(f"Hello {name}, in 5 years you will be {futureAge} years old.")