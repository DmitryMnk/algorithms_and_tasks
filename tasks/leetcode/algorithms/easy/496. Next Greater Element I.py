from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        result = []
        for i in range(len(nums2) - 1):
            table[nums2[i]] = {
                'index': i,
                'next': nums2[i + 1]
            }
        table[nums2[-1]] = {
            'index': len(nums2) - 1,
            'next': None
        }


        for j in nums1:
            index = table[j]['index']
            next = table[j]['next']
            if next is None:
                result.append(-1)
            else:
                while True:
                    if next is None:
                        result.append(-1)
                        break
                    if next > j:
                        result.append(next)
                        break
                    next = table[next]['next']
        return result



solution = Solution()

print(
    solution.nextGreaterElement(
    [4,1,2],
    [1,3,4,2]
    )
)