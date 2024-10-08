from typing import List
from collections import Counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    # t1 = Counter(nums1)
    # t2 = Counter(nums2)
    # result = []
    # for key, val in t1.items():
    #     if key in t2:
    #         for i in range(min(t1[key], t2[key])):
    #             result.append(key)
    #
    # return result

    count1 = Counter(nums1)
    count2 = Counter(nums2)
    intersection = count1 & count2
    nums = list(intersection.elements())
    return nums

print(intersect(
[1,2], [1,1]
))