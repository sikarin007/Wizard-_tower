import pygame
from abc import ABC, abstractmethod

class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass

class Goblin(Enemy):
    def attack(self):
        print("Goblin attacks")

