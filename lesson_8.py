###___EX_1___###
def add_one(some_list):
    num_str = ""
    for num in some_list:
        num_str += str(num)
    num = int(num_str)
    num += 1
    result = []
    for index in str(num):
        result.append(int(index))
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

print(add_one([1, 2, 3, 4]))