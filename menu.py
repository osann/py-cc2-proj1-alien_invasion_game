"""
Project I from Python Crash Course
By JH.osan
"""
import pygame

from button import Button

class Menu:
    def __init__(self, ai_game):
        self.window = ai_game.window
        self.window_rect = ai_game.window.get_rect()
        self.settings = ai_game.settings
        self.game_instance = ai_game

        self.current_menu = "main"

        self.font = pygame.font.SysFont(None, 100)

        # Menu buttons
        # Main Menu
        self.title = self.font.render("Alien Invasion!", True, (30, 200, 30), self.settings.bg_colour)
        self.title_rect = self.title.get_rect()
        self.title_rect.center = self.window_rect.center
        self.title_rect.y -= 150
        self.play_button = Button(self, "Play", -175, 0)
        self.bonus_button = Button(self, "Target Practice", 175, 0)
        self.settings_button = Button(self, "Settings", 0, 75)
        # Settings Menu
        self.easy_button = Button(self, "Easy", -325, 0)
        self.med_button = Button(self, "Medium", 0, 0)
        self.hard_button = Button(self, "Hard", 325, 0)
        self.back_button = Button(self, "Back", 0, 75)

    def draw_menu(self):
        if self.current_menu == "main":
            self._display_main_menu()
        elif self.current_menu == "settings":
            self._display_settings_menu()

    def return_to_main_menu(self):
        self.current_menu = "main"

    def _display_main_menu(self):
        self.window.blit(self.title, self.title_rect)
        self.play_button.draw_button()
        self.bonus_button.draw_button()
        self.settings_button.draw_button()

    def _display_settings_menu(self):
        self.easy_button.draw_button()
        self.med_button.draw_button()
        self.hard_button.draw_button()
        self.back_button.draw_button()

    def _check_buttons(self, mouse_pos):
        if self.current_menu == "main":
            self._check_play_button(mouse_pos)
            self._check_bonus_button(mouse_pos)
            self._check_settings_button(mouse_pos)
        elif self.current_menu == "settings":
            self._check_difficulty_buttons(mouse_pos)

    def _check_play_button(self, mouse_pos):
        if self.play_button.check_mouse_pos(mouse_pos):
            self.game_instance._start_game()

    def _check_bonus_button(self, mouse_pos):
        if self.bonus_button.check_mouse_pos(mouse_pos):
            self.game_instance._start_bonus_game()

    def _check_settings_button(self, mouse_pos):
        if self.settings_button.check_mouse_pos(mouse_pos):
            self.current_menu = "settings"

    def _check_difficulty_buttons(self, mouse_pos):
        self._un_highlight_buttons()
        if self.easy_button.check_mouse_pos(mouse_pos):
            self.settings.difficulty_easy()
            self.easy_button.highlight_button()
        if self.med_button.check_mouse_pos(mouse_pos):
            self.settings.difficulty_med()
            self.med_button.highlight_button()
        if self.hard_button.check_mouse_pos(mouse_pos):
            self.settings.difficulty_hard()
            self.hard_button.highlight_button()
        if self.back_button.check_mouse_pos(mouse_pos):
            self.current_menu = "main"

    def _un_highlight_buttons(self):
        self.easy_button.reset_colour()
        self.med_button.reset_colour()
        self.hard_button.reset_colour()