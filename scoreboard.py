"""
Project I from Python Crash Course
By JH.osan
"""
import pygame
from pygame.sprite import Group

from ship import Ship


class Scoreboard:

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.window = ai_game.window
        self.window_rect = self.window.get_rect()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats

        self.text_colour = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 48)
        self.hs_text_colour = (255, 0, 0)

        self.prep_score()
        self.prep_alien_hscore()
        self.prep_tp_hscore()
        self.prep_ships()

    def prep_score(self):
        self.score_img = self.font.render(self.return_rounded(self.game_stats.score), True, self.text_colour, self.settings.bg_colour)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.window_rect.right - 20
        self.score_rect.top = 60

    def prep_alien_hscore(self):
        self.ahscore_img = self.font.render(self.return_rounded(self.game_stats.aliens_high_score), True,
                                           self.hs_text_colour, self.settings.bg_colour)
        self.ahscore_rect = self.ahscore_img.get_rect()
        self.ahscore_rect.right = self.window_rect.right - 20
        self.ahscore_rect.top = 20

    def prep_tp_hscore(self):
        self.tphscore_img = self.font.render(self.return_rounded(self.game_stats.target_practice_high_score), True,
                                           self.hs_text_colour, self.settings.bg_colour)
        self.tphscore_rect = self.tphscore_img.get_rect()
        self.tphscore_rect.right = self.window_rect.right - 20
        self.tphscore_rect.top = 20

    def prep_ships(self):
        self.ships = Group()

        for i in range(self.game_stats.lives):
            ship = Ship(self.ai_game)
            ship.rect.x = 20 + i * ship.rect.width
            ship.rect.y = 20
            self.ships.add(ship)


    def return_rounded(self, score):
        rounded = round(score, -1)
        return "{:,}".format(rounded)

    def draw_score(self):
        self.window.blit(self.score_img, self.score_rect)
        if self.game_stats.game_active:
            self.window.blit(self.ahscore_img, self.ahscore_rect)
            self.ships.draw(self.window)
        elif self.game_stats.bonus_game_active:
            self.window.blit(self.tphscore_img, self.tphscore_rect)
            self.ships.draw(self.window)

    def check_alien_hscore(self):
        if self.game_stats.score > self.game_stats.aliens_high_score:
            self.game_stats.aliens_high_score = self.game_stats.score
            self.prep_alien_hscore()

    def check_tp_hscore(self):
        if self.game_stats.score > self.game_stats.target_practice_high_score:
            self.game_stats.target_practice_high_score = self.game_stats.score
            self.prep_tp_hscore()