from collections import deque
from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    # if k == 0:
    #     return False
    # items = deque()
    # for i in range(len(nums)):
    #     if nums[i] in items:
    #         return True
    #
    #     if len(items) < k:
    #         items.append(nums[i])
    #     else:
    #         if items:
    #             items.popleft()
    #         items.append(nums[i])
    # return False

    d = {}

    for i, n in enumerate(nums):
        if n in d and abs(i - d[n]) <= k:
            return True
        else:
            d[n] = i

    return False

print(
    contains_nearby_duplicate(
    [99, 122, 133, 99],
    2
    )
)