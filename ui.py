import pygame
from config import *


def get_font(size, bold=False):
    return pygame.font.SysFont("Segoe UI, Arial", size, bold=bold)


def draw_hud(screen, state, elapsed):
    f_main = get_font(24, True)
    f_stats = get_font(18, True)

    # Timer e Score
    time_left = max(0, int(GAME_DURATION - elapsed))
    screen.blit(f_main.render(f"TIME: {time_left}s", True, WHITE), (30, 30))
    screen.blit(f_main.render(f"SCORE: {state.score}", True, GREEN), (SCREEN_WIDTH - 150, 30))

    # Statistiche Corrette/Errate (HUD)
    correct_txt = f_stats.render(f"CORRECT: {state.correct_total}", True, GREEN)
    wrong_txt = f_stats.render(f"WRONG: {state.wrong_total}", True, RED)
    screen.blit(correct_txt, (30, 70))
    screen.blit(wrong_txt, (30, 95))

    # Moltiplicatore e Meter
    mult_txt = f_main.render(f"x{state.multiplier}", True, GOLD)
    screen.blit(mult_txt, (SCREEN_WIDTH - 150, 70))
    for i in range(4):
        color = CYAN if i < state.meter else (50, 50, 60)
        pygame.draw.rect(screen, color, (SCREEN_WIDTH - 150 + (i * 22), 105, 18, 8))

    # Fading Istruzioni (Progressivo)
    alpha = 255
    if state.correct_total >= 12:
        alpha = 0
    elif state.correct_total >= 8:
        alpha = 80
    elif state.correct_total >= 4:
        alpha = 160

    if alpha > 0:
        f_hint = get_font(18)
        t_hint = f_hint.render("TOP: PARI?", True, GRAY)
        b_hint = f_hint.render("BOTTOM: VOCALE?", True, GRAY)
        t_hint.set_alpha(alpha);
        b_hint.set_alpha(alpha)
        screen.blit(t_hint, (SCREEN_WIDTH // 2 - t_hint.get_width() // 2, 50))
        screen.blit(b_hint, (SCREEN_WIDTH // 2 - b_hint.get_width() // 2, SCREEN_HEIGHT - 70))


def draw_card(screen, trial, feedback_color=None):
    y_pos = TOP_POS[1] if trial.position == "TOP" else BOTTOM_POS[1]
    rect = pygame.Rect(0, 0, 140, 190)
    rect.center = (SCREEN_WIDTH // 2, y_pos)

    bg = feedback_color if feedback_color else (240, 240, 240)
    pygame.draw.rect(screen, bg, rect, border_radius=15)
    pygame.draw.rect(screen, (50, 50, 50), rect, width=3, border_radius=15)

    f_card = get_font(60, True)
    txt = f_card.render(f"{trial.letter}{trial.number}", True, BLACK if not feedback_color else WHITE)
    screen.blit(txt, (rect.centerx - txt.get_width() // 2, rect.centery - txt.get_height() // 2))


def draw_screen(screen, title, subtitle, stats=None, color=WHITE):
    screen.fill(BLACK)
    t_surf = get_font(50, True).render(title, True, color)
    screen.blit(t_surf, (SCREEN_WIDTH // 2 - t_surf.get_width() // 2, 120))

    if stats:
        f_stat = get_font(22)
        for i, line in enumerate(stats):
            s_surf = f_stat.render(line, True, WHITE)
            screen.blit(s_surf, (SCREEN_WIDTH // 2 - s_surf.get_width() // 2, 220 + i * 35))

    sub_surf = get_font(20).render(subtitle, True, GRAY)
    screen.blit(sub_surf, (SCREEN_WIDTH // 2 - sub_surf.get_width() // 2, SCREEN_HEIGHT - 100))
