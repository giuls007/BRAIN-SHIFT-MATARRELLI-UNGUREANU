import random
import string
from models import Trial
from rules import compute_expected_answer

def generate_trial(rng: random.Random) -> Trial:
    pos = rng.choice(["TOP", "BOTTOM"])
    let = rng.choice(string.ascii_uppercase)
    num = rng.randint(1, 9)
    ans = compute_expected_answer(pos, let, num)
    return Trial(pos, let, num, ans)
