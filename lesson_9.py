def difference(*args):
    if len(args) <= 1:
        return 0
    max_number = float(max(args))
    min_number = float(min(args))

    diff = round((max_number - min_number), 10)
    return diff

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'

print("OK")
print(difference())
print(difference(10, -2.2, 0, 8, 0.5))
