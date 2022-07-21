"""
Project I from Python Crash Course
By JH.osan
"""
import sys
import pygame
import time

from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Running instance of the game
    """

    def __init__(self):
        """Init the game, and resources"""
        pygame.init()
        self.settings = Settings()

        self.window = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height))
        pygame.display.set_caption("Alien Invasion: Side Scroller")

        self.ship = Ship(self)

    def run(self):
        """Begin running game loop"""
        running = True
        while running:
            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.window.fill(self.settings.bg_colour)
            self.ship.blitme()

            # Draw screen
            pygame.display.flip()
            time.sleep(5.0)


if __name__ == "__main__":
    instance = AlienInvasion()
    instance.run
