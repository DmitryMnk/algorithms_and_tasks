from typing import List


def triangular_sum(nums: List[int]) -> int:
    while len(nums) > 1:
        for i in range(len(nums) - 1):
            nums[i] = (nums[i] + nums[i + 1]) % 10
        nums.pop()
    return nums[0]

print(triangular_sum(
    [1,2,3,4,5]
))
