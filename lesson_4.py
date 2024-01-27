#EXERCISE_1

###____1____###
my_list = [0, 1, 0, 8, 6, 24, 3, 0]

zero_count = my_list.count(0)

for _ in range(zero_count):
    my_list.remove(0)
for _ in range(zero_count):
    my_list.append(0)

print(my_list)

###____2____###
my_list.sort(key=lambda x: x ==0)

print(my_list)

