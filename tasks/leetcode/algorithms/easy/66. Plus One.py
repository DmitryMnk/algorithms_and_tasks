from typing import List


def plus_one(digits: List[int]) -> List[int]:

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            break

        if i == 0:
            digits = [1] + digits

    return digits

print(
    plus_one(
        [9, 9]
    )
)