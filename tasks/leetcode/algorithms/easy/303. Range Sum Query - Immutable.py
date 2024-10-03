from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.curr_sum = [0]
        for i in range(len(nums)):
            self.curr_sum.append(nums[i] + self.curr_sum[-1])


    def sumRange(self, left: int, right: int) -> int:
        return self.curr_sum[right + 1] - self.curr_sum[left]

ar = NumArray([-2, 0, 3, -5, 2, -1])
print(ar.sumRange(0, 2))
print(ar.sumRange(2, 5))
print(ar.sumRange(0, 5))

