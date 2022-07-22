"""
Project I from Python Crash Course
By JH.osan
"""
import sys
import pygame

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

        # Init game window with fullscreen/windowed
        if self.settings.fullscreen_mode:
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings = self.window.get_rect().width
            self.settings = self.window.get_rect().height
        else:
            self.window = pygame.display.set_mode(
                (self.settings.window_width, self.settings.window_height))

        pygame.display.set_caption("Alien Invasion: Side Scroller")

        self.ship = Ship(self)

    def run(self):
        """Begin running game loop"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        """Continually watch for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.settings.debug_mode:  # Debug messages
                    print(event)

                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_w:
                    self.ship.moving_up = True
                if event.key == pygame.K_s:
                    self.ship.moving_down = True
                if event.key == pygame.K_a:
                    self.ship.moving_left = True
                if event.key == pygame.K_d:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.ship.moving_up = False
                if event.key == pygame.K_s:
                    self.ship.moving_down = False
                if event.key == pygame.K_a:
                    self.ship.moving_left = False
                if event.key == pygame.K_d:
                    self.ship.moving_right = False

    def _update_screen(self):
        """Update the Pygame window"""
        self.window.fill(self.settings.bg_colour)
        self.ship.blitme()

        # Draw screen
        pygame.display.flip()


if __name__ == "__main__":
    instance = AlienInvasion()
    instance.run()
