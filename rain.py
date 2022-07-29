"""
Project I from Python Crash Course
By JH.osan
"""
import pygame
from pygame.sprite import Sprite
from random import randint


class Rain(Sprite):
    """Handle rain effect"""

    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.window

        self.colour = self.settings.rain_colour
        self.speed = self.settings.rain_speed

        self.rect = pygame.Rect(0, 0, self.settings.rain_width, self.settings.rain_height)
        self.rect.bottom = 0

        self.y = float(self.rect.y)
        self.x = randint(0, self.settings.window_width)

    def update(self):
        """Moves the raindrop down"""
        self.y += self.settings.rain_speed
        self.rect.y = self.y

    def draw_rain(self):
        """Draws the rain on the background"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
