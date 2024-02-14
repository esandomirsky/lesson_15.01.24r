###___EX_1___###

def popular_words(text, words):
    pop_words_dict = {}
    text = text.lower()
    word_list = text.split()

    for pop_word in words:
        #if len(pop_word) == 1:
            pop_words_dict[pop_word] = word_list.count(pop_word)
       # else:
            #pop_words_dict[pop_word] = word_list.count(pop_word)

    return pop_words_dict

text = "'Hi! When I was One I had just begun When I was Two I was nearly new"
words = ["i", "was", "three", "near"]

assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

print(popular_words(text, words))

##___EX_2___###
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