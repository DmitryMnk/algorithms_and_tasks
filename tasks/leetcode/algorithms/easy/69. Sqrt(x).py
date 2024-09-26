def my_sqrt(x: int) -> int:
    left = 0
    right = x // 2 + 1

    while left <= right:
        middle = (left + right) // 2
        if middle ** 2 <= x < (middle + 1) ** 2:
            return middle
        elif x == (middle + 1) ** 2:
            return middle + 1
        elif x < middle ** 2:
            right = middle
        else:
            left = middle