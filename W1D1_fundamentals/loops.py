# Loops

# For Loop

# for(var i = 0; i < 5; i++) in JS
# * Start --- inclusive, optional - default 0
#! Stop --- EXCLUSIVE, required
# ? Step --- optional, increment value (-/+)

# ? for _iterator_ in _collection_ :

# 1 - 10
# for value in range(1, 11):
#     print(value)

# 1 - 10 jump by 2

# for i in range(1, 11, 2):
#     print(i)

# 100 - 1

# for x in range(100, 0, -20):
#     print(x)

# for letter in "hello":
#     print(letter)

# --- Loop over a list
animals_list = ["Dog", "Dragon", "Lion", "Bird"]
# # ? for _iterator_ in _collection_ :

# for one_animal in animals_list:
#     print(one_animal)


# for i in range(len(animals_list)):
#     print(i, animals_list[i])

# for index, animal in enumerate(animals_list):
#     print(index, animal)


# --- Loop over a dict
cat1 = {"name": "Cinnamon", "age": 2, "color": "orange"}
cat2 = {"name": "Meow", "age": 2, "color": "black"}

# for some_var in cat1:
#     print(some_var, cat1[some_var])

# for var in cat1.values():
#     print(var)

# for var in cat1.keys():
#     print(var)

# for key, value in cat2.items():
#     print(key, value)

# ("name", "Meow")
# ("age", 2)
# ("color", "black")
my_set = ("name", "Meow")
key, value = my_set

key = my_set[0]
value = my_set[1]

animals_list = ["Dog", "Dragon", "Bird"]

first_animal, second_animal, _ = animals_list

print(first_animal, second_animal)
