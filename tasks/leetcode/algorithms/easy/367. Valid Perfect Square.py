def isPerfectSquare(num: int) -> bool:

    while num > 2:
        num /= 2
    return num.is_integer()

print(
    isPerfectSquare(3)
)