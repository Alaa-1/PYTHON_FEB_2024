# ============= Wizard =============
from game_classes.character import Character


class Wizard(Character):

    def __init__(self, name):
        super().__init__(name, health=100, power=15, defense=30)

    def attack(self, enemy):

        print(f"[WIZARD ATTACK] \n {self.name} is attacking {enemy.name}")
        enemy.defend(self.power)

    def defend(self, damage):
        super().defend(damage)
        if self.health <= 40:
            self.health += 10
            print(f"[HEALING] {self.name} drunk a potion")
