"""
Project I from Python Crash Course
By JH.osan
"""


class Stats:
    """Track game statistics"""

    def __init__(self, ai_game):
        """Init game stats"""
        self.lives = 0
        self.score = 0
        self.target_practice_high_score = 0
        self.aliens_high_score = 0
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.bonus_game_active = False

    def reset_stats(self):
        """Reset statistics to default"""
        if self.score >= self.target_practice_high_score:
            self.target_practice_high_score = self.score
        elif self.score >= self.aliens_high_score:
            self.aliens_high_score = self.score

        self.score = 0
        self.lives = self.settings.max_lives
