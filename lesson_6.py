###___EXERSICE_#1___###

default_list = [
    {"name": "John", "age": 15},
    {"name": "Jim", "age": 35},
    {"name": "Jack", "age": 45},
    {"name": "James", "age": 15},
    {"name": "Jango", "age": 25}
]
min_age = min(person["age"] for person in default_list)
young_list = [person["name"] for person in default_list if person["age"] == min_age]

max_length = max(len(person["name"]) for person in default_list)
len_name_list = [person["name"] for person in default_list if len(person["name"]) == max_length]

sum_age = sum(person["age"] for person in default_list)
average_age_list = sum_age // len(default_list)

print(young_list)
print(len_name_list)
print(average_age_list)


###___EXERSICE_2___###

dict_1 = {1: 1, 2: 2, 3: 3, 4: 4}
dict_2 = {11: 11, 2: 22, 3: 33, 44: 44}

common_keys = [key for key in dict_1.keys() if key in dict_2]

unique_keys_in_dict1 = [key for key in dict_1.keys() if key not in dict_2]

new_dict = {key: dict_1[key] for key in unique_keys_in_dict1}

merger_dict = {}
for key, value in dict_1.items():
    if key in dict_2:
        merger_dict[key] = [value, dict_2[key]]
    else:
        merger_dict[key] = value
for key, value in dict_2.items():
    if key not in dict_1:
        merger_dict[key] = value

print(common_keys)
print(unique_keys_in_dict1)
print(new_dict)
print(merger_dict)
