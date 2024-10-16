from typing import List


def can_arrange(arr: List[int], k: int) -> bool:
    indexes = []

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) % k == 0 and i not in indexes and j not in indexes:
                indexes.append(i)
                indexes.append(j)
                break

    if len(indexes) == len(arr):
        return True
    return False

print(
    can_arrange(
[1,2,3,4,5,6], 10
    )
)