from robot import Robot
from dinosaur import Dinosaur
import random

class Battlefield:
    def __init__(self):
        self.robot = Robot('Optimus Prime')
        self.dinosaur = Dinosaur('Godzilla', (random.randrange(10,20)))

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print(f' Welcome to the Battle between {self.robot.name} and {self.dinosaur.name}')

    def battle_phase(self):
        while self.dinosaur.health > 0 and  self.robot.health > 0:
            self.dinosaur.attack(self.robot)
            if self.robot.health > 0:    
                self.robot.attack(self.dinosaur)
        
    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f'{self.robot.name} has been Victorious in Battle!!')
        else:
            print(f'{self.dinosaur.name} has been Victorious in Battle!!')