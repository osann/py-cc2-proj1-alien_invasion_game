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
        self.fullscreen_mode = False

        # Ship settings
        self.ship_speed = 1

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (224, 71, 255)

        # Alien settings
        self.alien_x_speed = 0.5
        self.aliens_limit = 5

        # Rain settings
        self.rain_speed = 1
        self.rain_colour = (0, 182, 207)
        self.rain_width = 5
        self.rain_height = 10
        self.raindrops_limit = 100
