from typing import List


def summary_ranges(nums: List[int]) -> List[str]:

    if not nums:
        return []
    if len(nums) == 1:
        return [str(nums[0])]

    result = []
    last_num = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            if last_num == nums[i - 1]:
                result.append(str(nums[i - 1]))
            else:
                s = f'{last_num}->{nums[i - 1]}'
                result.append(s)
            last_num = nums[i]

    if nums[-1] == nums[-2] + 1:
        result.append(f'{last_num}->{nums[-1]}')
    else:
        result.append(str(nums[-1]))

    return result

print(
    summary_ranges(
[0,1,2,4,5,7]
    )
)

