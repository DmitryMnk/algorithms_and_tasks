def arrangeCoins(n: int) -> int:

    result = (-1 + (1 + 8 * n) ** 0.5) // 2
    return int(result)

print(arrangeCoins(10))