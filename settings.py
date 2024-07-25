class Settings:

    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.top = 0
        self.screen_width = 1200
        self.screen_height = 800
        self.bottom = self.screen_height
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
