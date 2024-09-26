def climb_stairs(n: int) -> int:
    memo = {
        0: 1,
        1: 1,
        2: 2
    }
    if n == 0 or n == 1:
        return 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]

print(
    climb_stairs(4)
)