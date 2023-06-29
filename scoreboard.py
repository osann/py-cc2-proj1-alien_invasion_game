"""
Project I from Python Crash Course
By JH.osan
"""
import pygame


class Scoreboard:

    def __init__(self, ai_game):
        self.window = ai_game.window
        self.window_rect = self.window.get_rect()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats

        self.text_colour = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        rounded = round(self.game_stats.score, -1)
        score_str = "{:,}".format(rounded)
        self.score_img = self.font.render(score_str, True, self.text_colour, self.settings.bg_colour)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.window_rect.right - 20
        self.score_rect.top = 20

    def draw_score(self):
        self.window.blit(self.score_img, self.score_rect)