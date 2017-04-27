"""Brute force recursion for now."""


def nchange(x, coins, i=0):
    if x == 0:
        return 1
    if x < 0 or i > len(coins) - 1:
        return 0
    return nchange(x, coins, i + 1) + nchange(x - coins[i], coins, i)

print(nchange(200, [1, 2, 5, 10, 20, 50, 100, 200]))
