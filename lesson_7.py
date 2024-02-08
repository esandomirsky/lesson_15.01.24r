###___EX_1___###

def say_hi(name, age):

    return f"Hi! My name is, {name}, and I am {age} years old."

assert say_hi("Eugene", 32) == f"Hi! My name is, Eugene, and I am 32 years old.", 'Test1'
assert say_hi("Petro", 48) == f"Hi! My name is, Petro, and I am 48 years old.", 'Test2'

print("OK")

#print(say_hi("Stepan", "22"))

###___EX_2___###

def get_correct_sentence(text: str):
    corrected_text = text[0].upper() + text[1:]
    if not text.endswith("."):
        corrected_text += "."

    return corrected_text

assert get_correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert get_correct_sentence("hello") == "Hello.", 'Test2'
assert get_correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert get_correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert get_correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print("OK")
#print(get_correct_sentence("some text"))

###___EX_3_(lesson_6)___###

dict_1 = {1: 1, 2: 2, 3: 3, 4: 4}
dict_2 = {11: 11, 2: 22, 3: 33, 44: 44}


common_keys = list(set(dict_1).intersection(dict_2))
unique_keys_in_dict1 = list(set(dict_1).difference(dict_2))

print(common_keys)
print(unique_keys_in_dict1)