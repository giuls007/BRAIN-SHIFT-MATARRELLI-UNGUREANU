from models import GameState

def update_score(state: GameState, is_correct: bool) -> GameState:
    if is_correct:
        state.score += 50 * state.multiplier
        state.correct_total += 1
        state.current_streak += 1
        state.meter += 1

        if state.current_streak > state.best_streak:
            state.best_streak = state.current_streak

        if state.meter == 4:
            state.multiplier = min(state.multiplier + 1, 10)
            state.meter = 0
    else:
        state.wrong_total += 1
        state.current_streak = 0
        if state.meter > 0:
            state.meter = 0
        else:
            state.multiplier = max(state.multiplier - 1, 1)

    return state
