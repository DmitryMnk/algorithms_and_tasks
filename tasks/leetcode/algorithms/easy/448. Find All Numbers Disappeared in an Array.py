from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    add = [0] * (len(nums) + 1)
    result = []
    for i in nums:
        add[i] += 1

    for j in range(1, len(add)):
        if add[j] == 0:
            result.append(j)

    return result

print(
    findDisappearedNumbers(
        [4,3,2,7,8,2,3,1]
    )
)