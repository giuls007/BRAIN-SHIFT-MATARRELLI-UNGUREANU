import pygame

# Dimensioni e FPS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Timing e Regole
GAME_DURATION = 60  # secondi
FADING_STEPS = {
    "FULL": 4,    # 100% opacità fino a 4 corrette
    "MEDIUM": 8,  # 70% opacità
    "LOW": 12,    # 30% opacità
}

# Scoring Avanzato
BASE_POINTS = 50
MAX_MULTIPLIER = 10

# Colori
WHITE = (240, 240, 240)
BLACK = (15, 15, 20)
GRAY = (100, 100, 100)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
GOLD = (241, 196, 15)
CYAN = (52, 152, 219)

# Posizioni
TOP_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 40)
BOTTOM_POS = (SCREEN_WIDTH // 2, (3 * SCREEN_HEIGHT) // 4 - 40)
