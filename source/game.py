import pygame
from config import screen_width, screen_height
import pytmx.util_pygame import load_pygame

from source.systems.control import KeyboardInputProvider, IInputProvider
from source.entities.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.map = load_pygame('assets/map/map01.tmx')


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(60)








