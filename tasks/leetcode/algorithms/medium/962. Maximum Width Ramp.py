from typing import List


def maxWidthRamp(nums: List[int]) -> int:
    n = len(nums)
    stack = []

    for i in range(n):
        if not stack or nums[stack[-1]] > nums[i]:
            stack.append(i)

    for i in range(n - 1, 0, -1):

        while stack and nums[stack[-1]] <= nums[i]:

            ans = max(ans, i - stack[-1])
            stack.pop()

print(
    maxWidthRamp(
        [9,8,1,0,1,9,4,0,4,1]
    )
)
