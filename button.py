"""
Project I from Python Crash Course
By JH.osan
"""
import pygame


class Button:
    """
    Creates instance of a button on screen.
    """

    def __init__(self, ai_game, text, x_pos =0, y_pos = 0):
        """Init button"""
        self.window = ai_game.window
        self.window_size = ai_game.window.get_rect()
        self.settings = ai_game.settings

        self.width, self.height = 300, 50

        self.colour = self.settings.button_colour
        self.current_colour = self.colour
        self.colour_highlight = self.settings.button_highlight
        self.text_colour = (255, 255, 255)

        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.window_size.center
        self.rect.x += x_pos
        self.rect.y += y_pos

        self.text = text
        self._prep_text(self.text)

    def _prep_text(self, text):
        self.text_image = self.font.render(text, True, self.text_colour, self.current_colour)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        self.window.fill(self.current_colour, self.rect)
        self.window.blit(self.text_image, self.text_image_rect)

    def highlight_button(self):
        self.current_colour = self.colour_highlight
        self._prep_text(self.text)

    def reset_colour(self):
        self.current_colour = self.colour
        self._prep_text(self.text)

    def check_mouse_pos(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False
