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
        self.window_size = ai_game.window.get_rect()

        self.image = pygame.image.load('images/rocket.bmp')  # Load ship and calculate hitbox
        self.hitbox = self.image.get_rect()

        self.hitbox.midleft = self.window_size.midleft  # Place ship on the middle left of the window

        # Ship settings
        self.settings = ai_game.settings
        self.y_pos = float(self.hitbox.y)
        self.x_pos = float(self.hitbox.x)

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Moves the ship"""
        if self.moving_up and self.hitbox.top > 0:
            self.y_pos -= self.settings.ship_speed
        if self.moving_down and self.hitbox.bottom < self.window_size.bottom:
            self.y_pos += self.settings.ship_speed
        if self.moving_left and self.hitbox.left > 0:
            self.x_pos -= self.settings.ship_speed
        if self.moving_right and self.hitbox.centerx < (self.window_size.right / 3):
            # Limit player to first third of the screen
            self.x_pos += self.settings.ship_speed

        self.hitbox.y = self.y_pos
        self.hitbox.x = self.x_pos

    def blitme(self):
        """Draw ship"""
        self.window.blit(self.image, self.hitbox)
