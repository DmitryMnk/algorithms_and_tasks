from collections import deque
from typing import List


def move_zeroes(nums: List[int]) -> None:
    index = 0
    for i in nums:
        if i != 0:
            nums[index] = i
            index += 1

    for j in range(index, len(nums)):
        nums[j] = 0
    print(nums)

move_zeroes(
[0,1,0,3,12]
)

