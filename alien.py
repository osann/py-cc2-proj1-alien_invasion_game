"""
Project I from Python Crash Course
By JH.osan
"""
import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
    """A class managing alien targets"""

    def __init__(self, x_placement, y_placement):
        """Init alien object"""
        super().__init__()

        self.spawn_points = []

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = x_placement
        self.rect.y = y_placement

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Moves alien across the screen"""
        self.x -= self.settings.alien_x_speed
        self.rect.x = self.x


class AlienFactory:
    """A class to handle building alien waves"""

    def __init__(self, ai_game):
        """Init factory with dicts, lists, etc"""
        self.settings = ai_game.settings
        self.slots = {}
        self.slots_used = []
        self.aliens = pygame.sprite.Group()

        self.ghost_alien = Alien(0, 0)
        self.generate_slots()

    def build_wave(self):
        """Generates a wave of aliens"""
        for i in range(0, self.settings.aliens_limit):
            proposed_slot = randint(1, len(self.slots))
            while proposed_slot in self.slots_used:
                proposed_slot = randint(1, len(self.slots))
            self.slots_used.append(proposed_slot)

            self.build_alien(proposed_slot)

    def generate_slots(self):
        """Calculates how many slots and where they are"""
        num_of_slots = int(self.settings.window_height / self.ghost_alien.rect.height)
        for i in range(2, num_of_slots - 1):
            self.slots[f"slot:{i-1}"] = i * self.ghost_alien.rect.height
        if self.settings.debug_mode:
            print(self.slots)

    def build_alien(self, slot):
        """Builds an alien object and places it in the correct slot"""
        alien = Alien(
            self.settings.window_width, self.slots[f"slot:{slot}"])
        self.aliens.add(alien)
        if self.settings.debug_mode:
            print(f"new_alien_placement: {alien.y}")
