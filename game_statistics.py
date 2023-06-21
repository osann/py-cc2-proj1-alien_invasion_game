"""
Project I from Python Crash Course
By JH.osan
"""


class Stats:
    """Track game statistics"""

    def __init__(self, ai_game):
        """Init game stats"""
        self.lives = 0
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Reset statistics to default"""
        self.lives = self.settings.max_lives
