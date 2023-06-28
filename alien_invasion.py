"""
Project I from Python Crash Course
By JH.osan
"""
import sys
from random import randint
from time import sleep

import pygame

from bullet import Bullet
from rain import Rain
from settings import Settings
from ship import Ship
from alien import AlienFactory
from game_statistics import Stats
from button import Button
from target import Target
from menu import Menu


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
        self.target = Target(self)

        self.game_stats = Stats(self)
        self.menu = Menu(self)


    # -------------------- Game loop
    def run(self):
        """Begin running game loop"""
        while True:
            self._check_events()

            self._create_rain()
            self._update_rain()

            if not self.game_stats.game_active and not self.game_stats.bonus_game_active:
                self._update_menu_screen()

            if self.game_stats.game_active:
                self._update_aliens()
                self._update_bullets_normal()
                self.ship.update()
                self._update_game_screen()

            if self.game_stats.bonus_game_active:
                self._update_target()
                self._update_bullets_bonus()
                self.ship.update()
                self._update_bonus_game_screen()

    # -------------------- Update handlers
    def _update_game_screen(self):
        """Update the Pygame window"""
        self.window.fill(self.settings.bg_colour)
        self._update_ship_and_bullets()
        self.alien_factory.aliens.draw(self.window)
        for raindrop in self.rain.sprites():
            raindrop.draw_rain()

        # Draw screen
        pygame.display.flip()

    def _update_bonus_game_screen(self):
        self.window.fill(self.settings.bg_colour)
        self._update_ship_and_bullets()
        self.target.draw_target()
        for raindrop in self.rain.sprites():
            raindrop.draw_rain()

        pygame.display.flip()

    def _update_menu_screen(self):
        self.window.fill(self.settings.bg_colour)
        for raindrop in self.rain.sprites():
            raindrop.draw_rain()
        if not self.game_stats.game_active:
            self.menu.draw_menu()

        pygame.display.flip()

    def _update_ship_and_bullets(self):
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    # -------------------- Event handlers
    def _check_events(self):
        """Continually watch for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.settings.super_debug_mode:  # Debug messages
                    print(event)
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.menu._check_buttons(pygame.mouse.get_pos())

    def _check_keydown_events(self, event):
        """Checks KEYDOWN events"""
        # Other keys
        if event.key == pygame.K_ESCAPE:
            if not self.game_stats.game_active and not self.game_stats.bonus_game_active:
                if self.menu.current_menu == "settings":
                    self.menu.return_to_main_menu()
                else:
                    sys.exit(0)
            self.game_stats.game_active = False
            self.game_stats.bonus_game_active = False
            pygame.mouse.set_visible(True)

        if event.key == pygame.K_SPACE:
            if self.game_stats.game_active:
                self._fire_bullet()
            if self.game_stats.bonus_game_active:
                if not self.bullets:     # Limits ship to single shot
                    self._fire_bullet()
        if event.key == pygame.K_p:
            self._start_game()
        if event.key == pygame.K_b:
            self._start_bonus_game()

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

    # -------------------- Game flows
    def _start_game(self):
        if not self.game_stats.game_active:
            self.settings.init_dynamic_settings()
            self.game_stats.reset_stats()
            self.game_stats.game_active = True
            self._reset_game()
            self.alien_factory.build_wave()
            pygame.mouse.set_visible(False)

    def _reset_game(self):
        self.alien_factory.aliens.empty()
        self.bullets.empty()
        self.ship.centre_ship()
        self.target.centre_target()
        self.settings.init_dynamic_settings()

    def _start_bonus_game(self):
        if not self.game_stats.game_active:
            self.game_stats.reset_stats()
            self.game_stats.bonus_game_active = True
            self._reset_game()
            self.game_stats.lives = self.settings.max_lives_bonus
            pygame.mouse.set_visible(False)


    # -------------------- Ship functions
    def _fire_bullet(self):
        """Fire bullet object from ship"""
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def _update_bullets_normal(self):
        """Updates bullets in game, and removes bullets that are off-screen"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.x > self.settings.window_width:
                self.bullets.remove(bullet)

        self._check_bullet_collisions_normal()

        # if self.settings.debug_mode:
        #     print(f"no. bullets: {len(self.bullets)}")

    def _update_bullets_bonus(self):
        """Updates bullets and provides logic to lower score + lives if that target is missed"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.x > self.settings.window_width:
                self.bullets.empty()
                self.game_stats.target_practice_score -= 10
                self.game_stats.lives -= 1
                if self.game_stats.lives <= 0:
                    self.game_stats.bonus_game_active = False
                    pygame.mouse.set_visible(True)
                if self.settings.debug_mode:
                    print(f"score: {self.game_stats.target_practice_score}\nlives: {self.game_stats.lives}")

        self._check_bullet_collisions_bonus()

    def _check_bullet_collisions_normal(self):
        """Checks for collisions between aliens and bullets, builds new wave if no aliens"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.alien_factory.aliens, True, True
        )
        if not self.alien_factory.aliens:
            self.bullets.empty()
            self.alien_factory.build_wave()
            self.settings.increase_speed()

    def _check_bullet_collisions_bonus(self):
        """Detects a bullet hitting the target and updates the score"""
        collide = pygame.sprite.spritecollideany(self.target, self.bullets)
        if collide:
            self.settings.increase_speed()
            self.bullets.empty()
            self.game_stats.target_practice_score += 10
            if self.settings.debug_mode:
                print(f"score: {self.game_stats.target_practice_score}")

    def _ship_hit(self):
        """Response to getting hit by an alien"""
        if self.game_stats.lives > 1:
            self.game_stats.lives -= 1
            self.settings.decrease_speed()
            if self.settings.debug_mode:
                print(f"lives: {self.game_stats.lives}")
        else:
            self.game_stats.game_active = False
            pygame.mouse.set_visible(True)

        self._reset_game()
        self._update_game_screen()

        sleep(1)

    # -------------------- Alien functions
    def _update_aliens(self):
        """Updates alien movement, and removes aliens off-screen"""
        for alien in self.alien_factory.aliens:
            alien.update()

        if pygame.sprite.spritecollideany(self.ship, self.alien_factory.aliens):
            self._ship_hit()

        self._check_aliens_reached_end()

        # if self.settings.debug_mode:
        #     print(f"no. aliens: {len(self.alien_factory.aliens)}")

    def _check_aliens_reached_end(self):
        """Checks whether aliens have reached the end of the screen"""
        for alien in self.alien_factory.aliens.sprites():
            if alien.rect.left <= 0:
                self._ship_hit()
                break

    # -------------------- Rain functions
    def _update_rain(self):
        """Updates raindrops in game, removing drops that are no longer visible"""
        self.rain.update()
        for raindrop in self.rain.copy():
            if raindrop.y > self.settings.window_height:
                self.rain.remove(raindrop)
        # if self.settings.debug_mode:
        #     print(f"raindrops: {len(self.rain)}")

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

    # -------------------- Target functions
    def _update_target(self):
        self.target.update()
        self.target._check_target_hit_wall()

    # -------------------- End class AlienInvasion


# -------------------- Run game
if __name__ == "__main__":
    instance = AlienInvasion()
    instance.run()
