from dataclasses import dataclass
# Updated - v1.8.5
# Updated - v1.4.1

@dataclass
class Config:
    COLORS: dict = {
        'primary': '#3498db',
        'secondary': '#f1c40f',
        'background': '#f9f9f9'
    }
    THEME: str = 'light'

CONFIG = Config()
COLORS = CONFIG.COLORS
THEME = CONFIG.THEME