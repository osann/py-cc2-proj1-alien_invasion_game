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

        # Ship settings
        self.max_lives = 3

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

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        # Ship
        self.ship_speed = 0.75
        self.bullet_speed = 1.5

        # Aliens
        self.alien_x_speed = 0.5

        # Target
        self.target_movement_speed = 0.25

    def increase_speed(self):
        self.ship_speed *= self.speed_scaler
        self.bullet_speed *= self.speed_scaler
        self.alien_x_speed *= self.speed_scaler
        self.target_movement_speed *= self.speed_scaler

    # -------------------- End class Settings
