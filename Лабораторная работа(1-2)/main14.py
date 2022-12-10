import random


def get_upper(string_list):
    return str(string_list[random.randint(0, len(string_list)-1)]).upper()

# ---------------------- Точка входа


my_strings = [
    "Eins",
    "Zwei",
    "Drei",
    "Vier",
    "Fünf",
]

print(get_upper(my_strings))
print(get_upper(my_strings))
print(get_upper(my_strings))
print(get_upper(my_strings))
print(get_upper(my_strings))
