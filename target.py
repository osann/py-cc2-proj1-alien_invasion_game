"""
Project I from Python Crash Course
By JH.osan
"""
import pygame
from pygame.sprite import Sprite


class Target(Sprite):
    """
    Class to handle new target practice mini-game target
    """

    def __init__(self, ai_game):
        self.window = ai_game.window
        self.window_size = ai_game.window.get_rect()
        self.settings = ai_game.settings

        self.width, self.height = self.settings.target_width, self.settings.target_height
        self.colour = self.settings.target_colour

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.moving_up, self.moving_down = True, False
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.centre_target()

    def update(self):
        if self.moving_up:
            self.y -= self.settings.target_movement_speed
        elif self.moving_down:
            self.y += self.settings.target_movement_speed
        self.rect.y = self.y

    def draw_target(self):
        pygame.draw.rect(self.window, self.colour, self.rect)

    def centre_target(self):
        self.rect.midright = self.window_size.midright
        self.y = self.settings.window_height / 2
        self.rect.y = self.y

    def _check_target_hit_wall(self):
        if self.rect.top <= 0:
            self.moving_down = True
            self.moving_up = False
        elif self.rect.bottom >= self.settings.window_height:
            self.moving_down = False
            self.moving_up = True
