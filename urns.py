# %%
"""
You have 3 urns each containing 100 balls.
2 urns contain 99 red balls and 1 green ball.
1 urn contains 100 red balls.
You pick 1 urn at random and the first 99 balls you remove from the urn are all red.
What is the probability that the last ball is green?
"""
# %%

import random


def data():
    return {
        1: [1] * 99 + [0],
        2: [1] * 99 + [0],
        3: [1] * 100,
    }


def process(urns):
    urn_key, urn = random.choice(list(urns.items()))

    random.shuffle(urn)
    removed_balls = urn[:99]
    last_ball = urn[-1]

    # (probability all 99 are red, probability last ball is green)
    return (all(x == 1 for x in removed_balls), last_ball == 0)


trials = [process(data()) for _ in range(1_000_000)]
we_saw_99_reds = sum(x for x, _ in trials)
we_saw_last_green = sum(y for x, y in trials if x)
probability = we_saw_last_green / we_saw_99_reds

print(probability)
# wrong?
# 0.019456869574441753

# %%
