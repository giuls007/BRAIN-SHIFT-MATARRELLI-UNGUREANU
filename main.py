import pygame
import time
import random
from config import *
from states import GameState
import ui, generator, scoring, models, input_handler


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Brain Shift Pro")
    clock = pygame.time.Clock()

    rng = random.Random()
    game = models.GameState()
    trial = generator.generate_trial(rng)

    state = GameState.INTRO
    start_time = 0
    total_pause_time = 0
    feedback_end = 0
    f_color = None

    running = True
    while running:
        now = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            action = input_handler.handle_game_input(event)

            if action == "QUIT":
                running = False

            if state == GameState.INTRO and action == "START":
                state = GameState.PLAYING
                start_time = now

            elif state == GameState.PLAYING:
                if action == "TOGGLE_PAUSE":
                    state = GameState.PAUSE
                    p_start = now
                elif action in ["YES", "NO"]:
                    user_ans = (action == "YES")
                    is_ok = (user_ans == trial.expected_answer)
                    game = scoring.update_score(game, is_ok)
                    f_color = GREEN if is_ok else RED
                    feedback_end = now + 0.15
                    trial = generator.generate_trial(rng)

            elif state == GameState.PAUSE and action == "TOGGLE_PAUSE":
                state = GameState.PLAYING
                total_pause_time += (now - p_start)

            elif state == GameState.RESULTS and action == "RESTART":
                main();
                return

        screen.fill(BLACK)

        if state == GameState.INTRO:
            ui.draw_screen(screen, "BRAIN SHIFT", "Premi un tasto per iniziare", color=CYAN)

        elif state == GameState.PLAYING:
            elapsed = (now - start_time) - total_pause_time
            if elapsed >= GAME_DURATION: state = GameState.RESULTS
            ui.draw_hud(screen, game, elapsed)
            ui.draw_card(screen, trial, f_color if now < feedback_end else None)

        elif state == GameState.PAUSE:
            ui.draw_screen(screen, "PAUSA", "Premi 'P' per riprendere", color=GOLD)

        elif state == GameState.RESULTS:
            acc = (game.correct_total / (game.correct_total + game.wrong_total) * 100) if (game.correct_total + game.wrong_total) > 0 else 0
            stats = [f"Score: {game.score}", f"Corrette: {game.correct_total}", f"Errate: {game.wrong_total}",
                     f"Accuratezza: {acc:.1f}%"]
            ui.draw_screen(screen, "FINE SESSIONE", "R per Rigiocare - ESC per Uscire", stats=stats, color=GREEN)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
