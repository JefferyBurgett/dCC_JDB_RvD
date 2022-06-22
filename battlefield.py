from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner

    def display_welcome(self):
        print(f' Welcome to the Battle between {self.robot.name} and {self.dinosaur.name}')

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.dinosaur.attack(self.robot)
            self.robot.attack(self.dinosaur)
        if self.dinosaur.health <= 0:
            print(f'{self.robot.name} has won the Battle!')
            return
        elif self.robot.health <= 0:
            print(f'{self.dinosaur.name} has won the Battle!')
            return
        else:
            pass


    def display_winner(self):
        self.robot_winner = Robot()
        self.dinosaur_winner = Dinosaur()