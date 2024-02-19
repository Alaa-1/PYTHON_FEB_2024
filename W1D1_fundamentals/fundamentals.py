# * Fundamentals
# this is a one line comment

"""
this is a multiline
comment !
"""

# ==== Variables ====
# primitives
# snake_casing
my_float = 3.14
my_name = "Joe"
is_admin = False
my_number = 11

format_string = f"we can inject {my_number} variables here "

# print(format_string)
# print("my lucky number is, " + str(my_number))


# ==== composite types ====
# snake_casing
# -- Lists
# aka array in JS

my_numbers = [1, 2, 3, 4]
# print(my_numbers)
# adding new items to the end of list
# my_numbers.append(33)
# print(my_numbers)
# removing items from the end of the list
# my_numbers.pop()
# removing an item at specific index
# my_numbers.pop(0)
# print(my_numbers)

# print(my_numbers[-2])

# length of a list
# print(len(my_numbers))
# my_numbers[0] = 101
# print(my_numbers)

###### Slicing
#         0         1         2      3      4
words = ["start", "going", "till", "the", "end"]
# Sub-ranges (portions) of the list
# print(words[1:])  # ["going", "till", "the", "end"]
# print(words[1:3])  # ["going", "till"]
# print(words[:2])  # ["start", "going"]
# print(words[:])  # ["start", "going", "till", "the", "end"]

# print(words[-1:])


# ------- Dictionary
# aka objects in JS
# they are not indexed -> they have key-value pairs
dog_dict = {"name": "Spark", "age": 3, "color": "black", "is_trained": True}

# print(dog_dict)
# dog_owner = "John"

dog_dict["dog_owner"] = "John"
# print(dog_dict)

item_removed = dog_dict.pop("dog_owner")
# print(dog_dict)
# print(item_removed)

dog_dict2 = {
    "name": "Spark",
    "age": 3,
    "colors": ["black", "brown"],
    "is_trained": False,
}

# print(dog_dict2["colors"][1])

# del dog_dict2["age"]
# print(dog_dict2)

# if "Spark" in dog_dict2:
#     print(f"the dog's name is {dog_dict2['name']}")
# else:
#     print("name not found")

# --- TUPLES

# ---- immutable ---- cannot be changed
# indexed
my_tuple = (1, 3, 5, 7, {"name": "bob"}, [123, 200, 99])
print(type(my_tuple))


my_tuple[5][1] = 205
print(my_tuple)
