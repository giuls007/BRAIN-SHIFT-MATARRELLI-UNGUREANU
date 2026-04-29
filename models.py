from dataclasses import dataclass

@dataclass
class Trial:
    position: str
    letter: str
    number: int
    expected_answer: bool
    user_answer: bool | None = None
    is_correct: bool = False

@dataclass
class GameState:
    score: int = 0
    multiplier: int = 1
    meter: int = 0
    correct_total: int = 0
    wrong_total: int = 0
    best_streak: int = 0
    current_streak: int = 0
