"""
Project I from Python Crash Course
By JH.osan
"""
import sys
import pygame
from random import randint

from settings import Settings
from ship import Ship
from bullet import Bullet
from star import Star


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
            self.settings.window_width = self.window.get_rect().width
            self.settings.window_height = self.window.get_rect().height
        else:
            self.window = pygame.display.set_mode(
                (self.settings.window_width, self.settings.window_height))

        pygame.display.set_caption("Alien Invasion: Side Scroller")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_stars()

    def run(self):
        """Begin running game loop"""
        while True:
            self._check_events()
            self._update_bullets()
            self.ship.update()

            self._update_screen()

    def _update_bullets(self):
        """Updates bullets in game, and removes bullets that are off-screen"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.x > self.settings.window_width:
                self.bullets.remove(bullet)
        if self.settings.debug_mode:
            print(len(self.bullets))

    def _check_events(self):
        """Continually watch for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.settings.debug_mode:  # Debug messages
                    print(event)

                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Checks KEYDOWN events"""
        # Other keys
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

        # Movement keys
        if event.key == pygame.K_w:
            self.ship.moving_up = True
        if event.key == pygame.K_s:
            self.ship.moving_down = True
        if event.key == pygame.K_a:
            self.ship.moving_left = True
        if event.key == pygame.K_d:
            self.ship.moving_right = True

    def _check_keyup_events(self, event):
        """Checks KEYUP events"""
        # Movement keys
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
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.stars.draw(self.window)

        # Draw screen
        pygame.display.flip()

    def _fire_bullet(self):
        """Fire bullet object from ship"""
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def _create_stars(self):
        """Handles the creation of stars"""
        star = Star(self)
        star_width, star_height = star.rect.size

        available_space_x = (self.settings.window_width * 0.66) - 2 * star_width
        num_spaces = int(available_space_x // (2 * star_width))

        available_space_y = self.settings.window_height - (2 * star_height)
        num_spaces_y = int(available_space_y // (2 * star_height))

        if self.settings.debug_mode:
            print(f"{available_space_x} // (2 * {star_width}) = {num_spaces}")
            print(f"{available_space_x} // {2 * star_width} = {num_spaces}")
            print(f"{available_space_y} // (2 * {star_height}) = {num_spaces_y}")
            print(f"{available_space_y} // {2 * star_height} = {num_spaces_y}")

        for num_spaces_y in range(0, num_spaces_y):

            for star_num in range(0, num_spaces):
                self._create_star(star_num, num_spaces_y)

    def _create_star(self, star_num, num_spaces_y):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.rect.x = self.settings.window_width - ((star_width * 2) + 3 * star_width * star_num)
        star.rect.y = (2 * star_height) + 2 * star.rect.height * num_spaces_y

        star.rect.x = star.rect.x + (randint(-50, 50))
        star.rect.y = star.rect.y + (randint(-50, 50))

        self.stars.add(star)


if __name__ == "__main__":
    instance = AlienInvasion()
    instance.run()
