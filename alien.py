"""
Project I from Python Crash Course
By JH.osan
"""
import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
    """A class managing alien targets"""

    def __init__(self, ai_game):
        """Init alien object"""
        super().__init__()
        self.settings = ai_game.settings

        self.spawn_points = []

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.settings.window_width
        self.rect.y = randint(0, self.settings.window_height)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Moves alien across the screen"""
        self.x -= self.settings.alien_x_speed
        self.rect.x = self.x
