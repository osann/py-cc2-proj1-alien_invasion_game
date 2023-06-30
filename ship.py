"""
Project I from Python Crash Course
By JH.osan
"""
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """
    A class to manage the players ship
    """

    def __init__(self, ai_game):
        """Init players ship"""
        super().__init__()
        self.window = ai_game.window
        self.window_size = ai_game.window.get_rect()

        self.image = pygame.image.load('images/rocket.bmp')  # Load ship and calculate hitbox
        self.rect = self.image.get_rect()

        self.centre_ship()

        # Ship settings
        self.settings = ai_game.settings
        self.y_pos = float(self.rect.y)
        self.x_pos = float(self.rect.x)

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Moves the ship"""
        if self.moving_up and self.rect.top > 0:
            self.y_pos -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.window_size.bottom:
            self.y_pos += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x_pos -= self.settings.ship_speed
        if self.moving_right and self.rect.centerx < (self.window_size.right / 3):
            # Limit player to first third of the screen
            self.x_pos += self.settings.ship_speed

        self.rect.y = self.y_pos
        self.rect.x = self.x_pos

    def blitme(self):
        """Draw ship"""
        self.window.blit(self.image, self.rect)

    def centre_ship(self):
        self.rect.midleft = self.window_size.midleft
        self.y_pos = float(self.rect.y)
        self.x_pos = float(self.rect.x)

    # -------------------- End class Ship
