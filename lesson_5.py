###___UPDATED CALCULATOR___###

while True:
    number_1 = (input("Enter first number:"))
    operator = input("What do you want to do? (+, -, /, *):")
    number_2 = (input("Enter second number:"))
    result = 0

    if not (number_1.isdigit() or number_1.replace('.', '', 1).isdigit()):
        print("Invalid input! Please enter valid numbers.")
        continue
    if not (number_2.isdigit() or number_2.replace('.', '', 1).isdigit()):
        print("Invalid input! Please enter valid numbers.")
        continue

    number_1 = float(number_1)
    number_2 = float(number_2)

    if operator not in ("+", "-", "*", "/"):
        result = "Invalid input! Please enter valid symbols."
    elif operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    elif operator == "/" and number_2 == 0:
        result = "Cannot divide by zero!"
    elif operator == "/" and number_2 != 0:
        result = number_1 / number_2
    else:
        result = "Invalid input! Please enter valid numbers."

    print("Result:", result)

    choice = input("Do you want to do a new calculations? (yes/no): ")
    if choice.lower() != "yes":
        print("Goodbye!")
        break