def isPowerOfThree(n: int) -> bool:
    result = 0
    i = 1
    while result < n:
        result = 3 ** i
        if result == n:
            return True
        i += 1
    return False

print(
    isPowerOfThree(27)
)