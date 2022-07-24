"""
Project I from Python Crash Course
By JH.osan
"""
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Class that builds stars"""

    def __init__(self, ai_game):
        super().__init__()
        self.window = ai_game.window

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = ai_game.settings.window_width - (self.rect.width * 2)
        self.rect.y = self.rect.height / 2

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
