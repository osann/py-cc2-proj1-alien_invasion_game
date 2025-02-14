"""
Project I from Python Crash Course
By JH.osan
"""
import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
    """A class managing individual aliens"""

    def __init__(self, x_placement, y_placement, speed):
        """Init alien object"""
        super().__init__()
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = x_placement
        self.rect.y = y_placement
        self.speed = speed

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Moves alien across the screen"""
        self.x -= self.speed
        self.rect.x = self.x

    # -------------------- End class Alien


class AlienFactory:
    """A class to handle building alien waves"""

    def __init__(self, ai_game):
        """Init factory with dicts, lists, etc"""
        self.settings = ai_game.settings
        self.slots = {}
        self.aliens = pygame.sprite.Group()

        self.ghost_alien = Alien(0, 0, 0)
        self.generate_slots()

    def build_wave(self):
        """Generates a wave of aliens"""
        slots_used = []
        for i in range(0, self.settings.aliens_limit):
            proposed_slot = randint(1, len(self.slots))
            while proposed_slot in slots_used:
                proposed_slot = randint(1, len(self.slots))
            slots_used.append(proposed_slot)

            self.build_alien(proposed_slot)

    def generate_slots(self):
        """Calculates how many slots and where they are"""
        num_of_slots = int(self.settings.window_height / self.ghost_alien.rect.height)
        for i in range(1, num_of_slots - 1):
            self.slots[f"slot:{i}"] = i * self.ghost_alien.rect.height
        if self.settings.debug_mode:
            print(self.slots)

    def build_alien(self, slot):
        """Builds an alien object and places it in the correct slot"""
        alien = Alien(
            self.settings.window_width, self.slots[f"slot:{slot}"], self.settings.alien_x_speed)
        self.aliens.add(alien)
        if self.settings.debug_mode:
            print(f"new_alien_placement: {alien.y}")

    # -------------------- End class AlienFactory
