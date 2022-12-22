import random


def MonteCarlo(n):
    pi = 0
    circle_points = 0

    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            circle_points += 1

        pi = 4 * circle_points / n
    return pi


print(f"Przyblizona wartosc pi = {MonteCarlo(n = 1_000_000)}")
