from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.active_weapon = Weapon()

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} shoots {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} leaving them with {dinosaur.health} remaining')