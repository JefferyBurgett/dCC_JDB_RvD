class Dinosaur:
    def __init__(self, name, ap):
        self.name = name
        self.attack_power = ap
        self.health = 50

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} tail smashes {robot.name} for {self.attack_power} damage leaving {robot.name} with {robot.health} health remaining")
