# ============= Warrior =============
from game_classes.character import Character


class Warrior(Character):

    def __init__(self, name="kingdom_warrior"):
        super().__init__(name, health=100, power=10, defense=50)

    def attack(self, enemy):
        super().attack(enemy, 2)
        print(
            f"[Warrior Attack] {self.name} is using special attack against {enemy.name}"
        )
