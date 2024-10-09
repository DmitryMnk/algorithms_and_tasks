def guess(num: int) -> int:
    gs = 5
    if num < gs:
        return 1
    elif num == gs:
        return 0
    else:
        return -1


def guessNumber(n: int) -> int:
    left = 0
    right = n

    while left <= right:
        middle = (left + right) // 2
        result = guess(middle)
        if result == 0:
            return middle
        elif result == 1:
            left = middle + 1
        else:
            right = middle - 1


print(
    guessNumber(12)
)
