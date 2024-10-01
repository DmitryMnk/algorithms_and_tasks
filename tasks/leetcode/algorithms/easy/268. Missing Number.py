from typing import List


def missing_number(nums: List[int]) -> int:
    # temp = ['0'] * (len(nums) + 1)
    # for i in nums:
    #     temp[i] = 1
    #
    # if '0' in temp:
    #     return temp.index('0')
    # else:
    #     return len(nums)

    return len(nums) * (len(nums) + 1) // 2 - sum(nums)



print(
    missing_number(
        [0,1]
    )
)