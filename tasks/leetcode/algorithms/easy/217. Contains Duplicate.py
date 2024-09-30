from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    # table = dict()
    #
    # for n in nums:
    #     table.setdefault(n, 0)
    #     table[n] += 1
    #     if table[n] > 1:
    #         return True
    #
    # return False

    # s = set()
    #
    # for x in nums:
    #     if x in s:
    #
    #         return True
    #
    #     else:
    #
    #         s.add(x)
    #
    # return False

    dic_num = {}
    for i in nums:
        if i in dic_num:
            return True
        else:
            dic_num[i] = 1
    return False

print(contains_duplicate(
    [1,2,3,4]
))