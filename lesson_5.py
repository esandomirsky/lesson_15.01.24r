###___UPDATED CALCULATOR___###EXERCISE_#2

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

#######___VARIABLE_NAME___#####EXERCISE_#1

import string
import keyword

var_name = input("Enter your variable name:")

if var_name[0].isdigit():
    print("Invalid input!\nThe first symbol cannot begin of numbers")
elif var_name[0].isupper():
    print("Invalid input!\nThe first symbol cannot consist of capital letter")
elif var_name.isdigit():
    print("Invalid input!\nThe variable name cannot consist of only numbers")
elif any(char.isupper() for char in var_name):
    print("Invalid input!\nThe variable name cannot consist of capital letter")
elif any(char in string.punctuation.replace('_', '') or char == ' ' for char in var_name):
    print("Invalid input!\nThe variable name cannot consist of punctuation or 'space'")
elif var_name in keyword.kwlist:
    print("Invalid input!\nThe variable name is already reserved by python")
else:
    print("Your variable name confirm!")

######___THE_SECRET_CODE_TO_NICK___####EXERCISE_*

