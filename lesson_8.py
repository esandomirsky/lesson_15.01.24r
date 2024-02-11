###___EX_1___###
def add_one(some_list):
    num_str = ""
    for num in some_list:
        num_str += str(num)
    num = int(num_str)
    num += 1
    result = []
    for element in str(num):
        result.append(int(element))
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

#print(add_one([1, 2, 3, 4]))

###___EX_2___###

def find_unique_value(some_list):
    unique_value = None
    for num in some_list:
        if some_list.count(num) == 1:
            unique_value = num
            break
    return unique_value

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
#print(find_unique_value([5, 2, 2, 5, 8, 0.222, 8]))