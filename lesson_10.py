###___EX_1___###

def pow(x):
    return x ** 2

def some_gen(begin, end, func):

    start = begin
    count = 0

    while count < end:
        yield start
        start = func(start)
        count += 1

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

#gen = some_gen(2, 4, pow)
#print(list(gen))

###___EX_2___###

def is_even(digit):

    if digit % 2 == 0:
        return True
    else:
        return False

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')