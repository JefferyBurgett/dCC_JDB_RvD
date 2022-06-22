from sys import api_version
from unicodedata import name


class Dinosaur:
    def __init__(self, name, ap):
        self.name = name
        self.attack_power = ap
        self.health = 50