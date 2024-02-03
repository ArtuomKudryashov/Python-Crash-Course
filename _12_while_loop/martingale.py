import random
HEADS = "heads"
TAILS = "tails"

COIN_VALUES = [HEADS, TAILS]

def flip_coin():
    return random.choice(COIN_VALUES)


print(flip_coin())


def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int)->int:
    steps_to_loops = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds>0:
        steps_to_loops+=1
        current_funds=current_funds-current_bet

