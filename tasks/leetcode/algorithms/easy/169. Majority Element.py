from typing import List


def majority_element(nums: List[int]) -> int:
    # table = dict()
    #
    # for i in nums:
    #     table.setdefault(i, 0)
    #     table[i] += 1
    #
    # for key, val in table.items():
    #     if val > len(nums) // 2:
    #         return key

    most_seen = 0
    times_seen = 0
    for i in nums:
        if times_seen == 0:
            most_seen = i
            times_seen += 1
        elif most_seen == i:
            times_seen += 1
        else:
            times_seen -= 1
    return most_seen

print(
    majority_element(
        [2,2,1,1,1,2,2]
    )
)