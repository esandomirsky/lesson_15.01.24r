
#########CALCULATOR#########

number_1 = float(input("Enter first number:"))
function = input("What do you want to do? (+, -, /, *):")
number_2 = float(input("Enter second number:"))

if function == "+":
    result_plus = number_1 + number_2
    print("Result: " + str(result_plus))
elif function == "-":
     result_min = number_1 - number_2
     print("Result: " + str(result_min))
elif function == "*":
    result_mul = number_1 * number_2
    print("Result: " + str(result_mul))
elif function == "/":
    if number_2 != 0:
        result_div = number_1 / number_2
        print("Result: " + str(result_div))
    else:
          print("Cannot divide by zero!")
else:
    print("Error!")