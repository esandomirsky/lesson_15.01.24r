####___EX_1___###
def prime_generator(end):
    def is_prime(num):
        if num < 2:
            return False
        for divider in range(2, int(num ** 0.5)+1):
            if num % divider == 0:
                return False
        return True

    num = 2
    while num <= end:
        if is_prime(num):
            yield num
        num += 1

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')


####___EX_2___###
def is_even(number):
    if number & 1 == 0:
        return True
    else:
        return False


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('Ok')