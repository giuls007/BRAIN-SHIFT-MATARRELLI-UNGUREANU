import pygame

def handle_game_input(event):
    """Traduce i tasti fisici in azioni logiche."""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            return "QUIT"
        if event.key == pygame.K_p:
            return "TOGGLE_PAUSE"
        if event.key == pygame.K_RIGHT:
            return "YES"
        if event.key == pygame.K_LEFT:
            return "NO"
        if event.key == pygame.K_r:
            return "RESTART"
        # Qualsiasi tasto per iniziare dall'intro
        return "START"
    return None
