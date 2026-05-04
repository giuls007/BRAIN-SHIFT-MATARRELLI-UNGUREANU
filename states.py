from enum import Enum, auto

class GameState(Enum):
    INTRO = auto()
    PLAYING = auto()
    PAUSE = auto()
    RESULTS = auto()
