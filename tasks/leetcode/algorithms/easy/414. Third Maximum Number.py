from typing import List


def thirdMax(nums: List[int]) -> int:
    first_max = float('-inf')
    second_max = float('-inf')
    third_max = float('-inf')

    for i in nums:
        if i > first_max:
            third_max = second_max
            second_max = first_max
            first_max = i
        elif first_max > i > second_max:
            third_max = second_max
            second_max = i
        elif second_max > i > third_max:
            third_max = i
    if third_max == float('-inf'):
        return first_max

    return(third_max)


print(
    thirdMax(
        [-1,2]
    )
)