import random

from game_classes.warrior import Warrior
from game_classes.wizard import Wizard

bob = Warrior("Bob")
voldemort = Wizard("voldemort")

# bob.attack(voldemort)


while bob.health > 0 and voldemort.health > 0:
    print("Welcome to the game, what shall we do !!")
    response = ""

    response = input("What do we do ? \n 1)attack 2)display stats \n")

    # player
    if response == "1":
        bob.attack(voldemort)
    elif response == "2":
        bob.display_stats()
        voldemort.display_stats()

    else:
        print(">>> please choose a valid response <<<")

    print("=" * 50)

    # CPU
    computer_response = random.randint(1, 2)
    if computer_response == 1:
        voldemort.attack(bob)
    else:
        bob.display_stats()
        voldemort.display_stats()
