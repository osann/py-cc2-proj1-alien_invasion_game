"""
Project I from Python Crash Course
By JH.osan
"""
import pygame


class Ship:
    """
    A class to manage the players ship
    """

    def __init__(self, ai_game):
        """Init players ship"""
        self.window = ai_game.window
        self.screen_rect = ai_game.window.get_rect()

        self.image = pygame.image.load('images/rocket.bmp')
        self.hitbox = self.image.get_rect()

        self.hitbox.center = self.screen_rect.center

    def blitme(self):
        """Draw ship"""
        self.screen.blit(self.image, self.hitbox)
