# # template or blueprint (Ninja)


# class Ninja:
#     # class attributes/variables
#     dojo_name = "Coding Dojo"
#     all_ninjas = []

#     # CONSTRUCTOR -> Create Defaults
#     def __init__(self, name, age, weapon, strength, is_sensei):
#         # instance variables / attributes
#         self.name = name
#         self.age = age
#         self.weapon = weapon
#         self.strength = strength
#         self.health = 1000
#         self.is_sensei = is_sensei
#         # every time we create an instance we add it to the list
#         Ninja.all_ninjas.append(self)

#     # Methods / Actions
#     def display_stats(self):
#         print(
#             f"{self.name}, is {self.age} years old and his weapon is a {self.weapon.type}. His health is {self.health} HP "
#         )

#     def eat_pizza(self):
#         self.strength += 10
#         print(f"{self.name} ate a pizza and their strength is {self.strength}")

#     def attack(self, another_instance):
#         another_instance.health -= self.strength

#         print(
#             f"[ATTACK] {self.name} attacks {another_instance.name} with a {self.weapon} and they receive {self.strength} damage"
#         )
#         return self

#     @classmethod
#     def party(cls):

#         for one_ninja in cls.all_ninjas:
#             one_ninja.eat_pizza()

#     @staticmethod
#     def check_age(age):
#         if age < 18:
#             print("Go Home !")
#         else:
#             print("Welcome !!")


# # instantiate the Ninja class

# # ninja1 = Ninja("Leo", 18, "Sword", 999, False)
# # ninja2 = Ninja("Miky", 18, "nunchuks", 533, False)

# # ninja1.attack()
# # ninja2.display_stats()
# # # ninja1.eat_pizza()
# # # ninja2.eat_pizza()
# # print("=" * 50)
# # ninja1.attack(ninja2).attack(ninja2).attack(ninja2)
# # print("=" * 50)

# # ninja2.display_stats()

# # print(Ninja.all_ninjas)
# # print("=" * 50)

# # Ninja.party()

# # ninja1.check_age(ninja1.age)

# # ======================= WEAPON ===========================


class Weapon:
    # CONSTRUCTOR
    def __init__(self, data):
        self.type = data["type"]
        self.damage = data["damage"]


# # instantiate the weapon class

# lethal_weapon = Weapon("Katana", 105)

# print(lethal_weapon.type)

# Shredder = Ninja("Shredder", 800, lethal_weapon, 5000, True)

# Shredder.display_stats()


# * ============= OOP & DICT practice ===============


# class Ninja:

#     # CONSTRUCTOR -> Create Defaults
#     def __init__(self, ninja_dict):
#         # instance variables / attributes
#         self.name = ninja_dict["name"]
#         self.age = ninja_dict["age"]
#         self.weapon = ninja_dict["weapon"]
#         self.strength = ninja_dict["strength"]
#         self.is_sensei = ninja_dict["is_sensei"]


# class Weapon:
#     # CONSTRUCTOR
#     def __init__(self, data):
#         self.type = data["type"]
#         self.damage = data["damage"]


# # Literal Object / Dictionay
# ninja1 = {
#     "name": "Donatelo",
#     "age": 20,
#     "weapon": "Staff",
#     "strength": 1000,
#     "is_sensei": False,
#     "type": "Sword",
#     "damage": 320,
# }


# donat = Ninja(ninja1)
# weapon1 = Weapon(ninja1)
# print(donat.name)
# print(weapon1.type)
