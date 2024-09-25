from typing import List


def remove_duplicates(nums: List[int]):
    if len(nums) <= 2:
        return len(nums)

    j = 2
    for i in range(1, len(nums)):
        if nums[i] != nums[j - 2]:
            nums[j] = nums[i]
            j += 1
    return j
