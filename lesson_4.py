#EXERCISE_1

###____1____###
my_list = [0, 1, 0, 8, 6, 24, 3, 0]

zero_count = my_list.count(0)

for number in range(zero_count):
    my_list.remove(0)
for number in range(zero_count):
    my_list.append(0)

print(my_list)

###____2____###
my_list = [0, 1, 0, 8, 6, 24, 3, 0]

my_list.sort(key=lambda x: x ==0)

print(my_list)


#EXERCISE_2

###____1____###
my_list = [1, 2, 3, 4, 5]
index = 0

for number in range(0, len(my_list), 2):
    index += my_list[number]
    result = my_list[-1] * index

print(result)

###____2____###
my_list = [1, 2, 3, 4, 5]

index_sum = sum(my_list[::2])
result = my_list[-1] * index_sum

print(result)