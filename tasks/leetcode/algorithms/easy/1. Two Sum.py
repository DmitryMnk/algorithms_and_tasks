from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    table = dict()

    for i in range(len(nums)):
        second_num = target - nums[i]
        first_index = table.get(second_num)
        if first_index is not None:
            return [first_index, i]
        table[nums[i]] = i
