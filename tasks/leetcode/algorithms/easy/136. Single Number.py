from typing import List


def singleNumber(nums: List[int]) -> int:
    temp = {}

    # for i in nums:
    #     temp.setdefault(i, 0)
    #     temp[i] += 1
    #
    # for key, val in temp.items():
    #     if val == 1:
    #         return key
    result = 0
    for number in nums:
        result ^= number
    return result

print(
    singleNumber(
        [-1]
    )
)
