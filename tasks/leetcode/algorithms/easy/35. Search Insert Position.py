from typing import List


def search_insert(nums: List[int], target: int) -> int:
    length = len(nums)
    left = 0
    right = length - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return left


print(search_insert(
[1,3,5,6],
7
))