from collections import deque
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if n == 0:
        return

    for i in range(len(nums1) - 1, -1, -1):
        if nums1[m - 1] > nums2[n - 1]:
            nums1[i] = nums1[m - 1]
            m -= 1
        else:
            nums1[i] = nums2[n - 1]
            n -= 1
        if m == 0 or n == 0:
            break
    if m == 0:
        for i in range(n - 1, -1, -1):
            nums1[i] = nums2[i]
