# DRY
# Don't Repeat Yourself
# === OOP ===
# Object Oriented Programming

# dict
# object literals
dog1 = {"name": "Apolo", "age": 2, "breed": "black lab"}
dog2 = {"name": "Spark", "age": 5, "breed": "german shapperd"}
dog3 = {"name": "Spot", "age": 1, "breed": "malti poo"}

# ? class
# ? template or blueprint for our instances(object)


# ------------------- CREATE A CLASS -------------------
class Dog:

    # constructor ->  creates defaults and builds and instance
    def __init__(self, name, age, breed="Labrador"):
        self.name = name
        self.age = age
        self.breed = breed

    # Methods / Actions
    def bark(self):
        print(f"{self.name} is making a loud WOOF !")

    def display_info(self):
        print(f"{self.name} is {self.age} years old, and their breed is {self.breed}")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name} for your {self.age} birthday 🎈🎈")

    # def __repr__(self):
    #     return f"{self.name} is {self.age} years old, and their breed is {self.breed}"


# instaniate the dog class
my_dog = Dog("Spark", 5, "german shapered")  # instance / object
fav_dog = Dog("Apolo", 1, "spanish shapered")  # instance / object
random_dog = Dog("unknown", 1, "black lab")  # instance / object
mascott = Dog("Paul", 1, "whatever")  # instance / object

# my_dog.birthday()
# print(my_dog.age)
