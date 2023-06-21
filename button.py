"""
Project I from Python Crash Course
By JH.osan
"""
import pygame


class Button:
    """
    Creates instance of a button on screen.
    """

    def __init__(self, ai_game, text):
        """Init button"""
        self.window = ai_game.window
        self.window_size = ai_game.window.get_rect()

        self.width, self.height = 200, 50
        self.colour = (255, 0, 255)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.window_size.center

        self._prep_text(text)

    def _prep_text(self, text):
        self.text_image = self.font.render(text, True, self.text_colour, self.colour)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        self.window.fill(self.colour, self.rect)
        self.window.blit(self.text_image, self.text_image_rect)
