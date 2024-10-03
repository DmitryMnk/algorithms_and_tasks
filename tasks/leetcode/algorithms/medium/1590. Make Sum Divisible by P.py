from typing import List

from attr.validators import min_len


def min_subarray(nums: List[int], p: int) -> int:
    array_sum = sum(nums)
    target = array_sum % p
    if target == 0:
        return 0

    table = {0: -1}
    prefix_sum = 0
    min_length = len(nums)
    for i, num in enumerate(nums):
        prefix_sum += num
        reminder = prefix_sum % p
        target_rem = (reminder - target + p) % p
        if target_rem in table:
            min_length = min(min_length, i - table[target_rem])

        table[reminder] = i

    return min_length if min_length < len(nums) else -1

print(
    min_subarray(
        [3, 1, 4, 2], 6
    )
)