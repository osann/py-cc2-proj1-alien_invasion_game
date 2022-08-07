"""
Project I from Python Crash Course
By JH.osan
"""
import sys
from random import randint

import pygame

from bullet import Bullet
from rain import Rain
from settings import Settings
from ship import Ship
from alien import AlienFactory


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
        self.rain = pygame.sprite.Group()

        self.alien_factory = AlienFactory(self)
        self.alien_factory.build_wave()

    # -------------------- Game loop
    def run(self):
        """Begin running game loop"""
        while True:
            self._check_events()

            self._create_rain()
            self._update_rain()

            self.alien_factory.update_aliens()

            self._update_bullets()
            self.ship.update()

            self._update_screen()

    # -------------------- Update handlers
    def _update_screen(self):
        """Update the Pygame window"""
        self.window.fill(self.settings.bg_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alien_factory.aliens.draw(self.window)
        for raindrop in self.rain.sprites():
            raindrop.draw_rain()

        # Draw screen
        pygame.display.flip()

    # -------------------- Event handlers
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

    # -------------------- Ship functions
    def _fire_bullet(self):
        """Fire bullet object from ship"""
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def _update_bullets(self):
        """Updates bullets in game, and removes bullets that are off-screen"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.x > self.settings.window_width:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.alien_factory.aliens, True, True
        )

        if not self.alien_factory.aliens:
            self.bullets.empty()
            self.alien_factory.build_wave()

        if self.settings.debug_mode:
            print(f"no. bullets: {len(self.bullets)}")

    # -------------------- Rain functions
    def _update_rain(self):
        """Updates raindrops in game, removing drops that are no longer visible"""
        self.rain.update()
        for raindrop in self.rain.copy():
            if raindrop.y > self.settings.window_height:
                self.rain.remove(raindrop)
        if self.settings.debug_mode:
            print(f"raindrops: {len(self.rain)}")

    def _create_rain(self):
        """Creates rain effect"""
        if len(self.rain) <= self.settings.raindrops_limit - 1:
            self._create_raindrop()

    def _create_raindrop(self):
        """Creates the raindrop"""
        raindrop = Rain(self)
        raindrop.rect.x = raindrop.x
        raindrop.y = randint(0, self.settings.window_height) - self.settings.window_height
        self.rain.add(raindrop)

    # -------------------- End class AlienInvasion


# -------------------- Run game
if __name__ == "__main__":
    instance = AlienInvasion()
    instance.run()
