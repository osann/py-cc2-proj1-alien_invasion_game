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
        self.window_width = 1200
        self.window_height = 800
        self.bg_colour = (176, 229, 233)

        # Mode settings
        self.debug_mode = True
        self.fullscreen_mode = False    # Receive strange int class errors when True

        # Ship settings
        self.ship_speed = 1

        # Bullet settings
        self.bullet_speed = 0.75
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (224, 71, 255)
