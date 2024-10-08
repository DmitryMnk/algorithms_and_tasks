from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    # s1 = set(nums1)
    # s2 = set(nums2)
    #
    # return list(s1.intersection(s2))
    if len(nums1) < len(nums2):
        minimal = nums1
        maximal = nums2
    else:
        minimal = nums2
        maximal = nums1

    result = list()
    for i in minimal:
        if i in maximal and i not in result:
            result.append(i)

    return result



print(
    intersection([1,2,2,1], [2,2])
)