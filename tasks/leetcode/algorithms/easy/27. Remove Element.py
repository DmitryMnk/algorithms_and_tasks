from collections import deque
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    indexes = deque()
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            indexes.append(i)
        else:
            count += 1
            if indexes:
                index = indexes.popleft()
                nums[index] = nums[i]
                indexes.append(i)
    return count
