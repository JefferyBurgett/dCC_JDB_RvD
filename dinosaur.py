import random
class Dinosaur:
    def __init__(self, name, ap):
        self.name = name
        self.attack_power = ap
        self.health = 50

    def attack(self, robot):
        damage = self.attack_power + random.randrange(1,10)
        robot.health -= damage
        print(f"{self.name} tail smashes {robot.name} for {damage} damage leaving {robot.name} with {robot.health} health remaining")
