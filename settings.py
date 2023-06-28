"""
Project I from Python Crash Course
By JH.osan
"""


class Settings:
    """
    A class to store all the various settings in Alien Invasion
    """
    def __init__(self):
        """Init game settings"""
        # Window settings
        self.window_width = 1920
        self.window_height = 1080
        self.bg_colour = (176, 229, 233)

        # Mode settings
        self.debug_mode = True
        self.super_debug_mode = False
        self.fullscreen_mode = False

        # Life settings
        self.max_lives = 3
        self.max_lives_bonus = 6

        # Bullet settings
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_colour = (224, 71, 255)

        # Alien settings
        self.aliens_limit = 5

        # Rain settings
        self.rain_speed = 1
        self.rain_colour = (0, 182, 207)
        self.rain_width = 5
        self.rain_height = 10
        self.raindrops_limit = 100

        # Target settings
        self.target_width = 50
        self.target_height = 200
        self.target_colour = (255, 0, 0)

        # Speed scaler
        self.speed_scaler = 1.2
        self.neg_speed_scaler = 0.6

        # Menu Colours
        self.button_colour = (255, 0 ,255)
        self.button_highlight = (0, 0, 255)

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        # Ship
        self.ship_speed = 0.5
        self.bullet_speed = 1

        # Aliens
        self.alien_x_speed = 0.2

        # Target
        self.target_movement_speed = 0.1

    def increase_speed(self):
        self.ship_speed *= self.speed_scaler
        self.bullet_speed *= self.speed_scaler
        self.alien_x_speed *= self.speed_scaler
        self.target_movement_speed *= self.speed_scaler

    def decrease_speed(self):
        self.ship_speed *= self.neg_speed_scaler
        self.bullet_speed *= self.neg_speed_scaler
        self.alien_x_speed *= self.neg_speed_scaler
        self.target_movement_speed *= self.neg_speed_scaler

    def difficulty_easy(self):
        self.speed_scaler = 1.1
        self.neg_speed_scaler = 0.8
        if self.debug_mode:
            print(f"difficulty: easy speed_scaler: {self.speed_scaler} neg_speed_scaler: {self.neg_speed_scaler}")

    def difficulty_med(self):
        self.speed_scaler = 1.2
        self.neg_speed_scaler = 0.6
        if self.debug_mode:
            print(f"difficulty: medium speed_scaler: {self.speed_scaler} neg_speed_scaler: {self.neg_speed_scaler}")


    def difficulty_hard(self):
        self.speed_scaler = 1.4
        self.neg_speed_scaler = 0.6
        if self.debug_mode:
            print(f"difficulty: hard speed_scaler: {self.speed_scaler} neg_speed_scaler: {self.neg_speed_scaler}")

    # -------------------- End class Settings
