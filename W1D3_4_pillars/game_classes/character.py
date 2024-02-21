class Character:

    # Constructor
    def __init__(self, name, health, power, defense):
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense

    # Methods

    def display_stats(self):
        print(
            f"[STATS] \n {self.name} has {self.health} HP.\n Power: {self.power}. \n Defense: {self.defense}"
        )

    def attack(self, enemy, multiply=1):
        print(f"[CHARACTER ATTACK] \n {self.name} is attacking {enemy.name}")
        enemy.defend(self.power)

    def defend(self, damage):
        self.health -= damage
        print(
            f"[CHARACTER DEFENSE] \n {self.name} takes {damage} DMG and they are now at {self.health} HP."
        )


# character1 = Character("John", 300, 999, 100)
# Villain = Character("Max", 800, 10000, 30)

# character1.display_stats()

# character1.attack(Villain)
