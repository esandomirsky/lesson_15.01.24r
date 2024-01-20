user_number = input("Please enter your 4-digit number: ") #1234

value_1 = 1000
value_2 = 100
value_3 = 10

result_1 = int(user_number) // int(value_1)
result_2 = (int(user_number) % int(value_1)) // int(value_2)
result_3 = (int(user_number) % int(value_2)) // int(value_3)
result_4 = int(user_number) % int(value_3)

print(result_1)
print(result_2)
print(result_3)
print(result_4)
