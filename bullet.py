"""
Project I from Python Crash Course
By JH.osan
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Bullet object logic for ship"""

    def __init__(self, ai_game):
        """Create and launch bullet at ships point"""
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.window
        self.colour = self.settings.bullet_colour

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.hitbox.midright

        self.x = float(self.rect.x)

    def update(self):
        """Updates objects of Bullet to move"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draws object to screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
