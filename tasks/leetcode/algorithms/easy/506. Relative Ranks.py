from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = []
        table = {}
        ns = sorted(score.copy(), reverse=True)

        for i in range(len(ns)):
            if i == 0:
                res = "Gold Medal"
            elif i == 1:
                res = "Silver Medal"
            elif i == 2:
                res = "Bronze Medal"
            else:
                res = str(i + 1)
            table[ns[i]] = res

        for n in score:
            result.append(table[n])
        return result


solution = Solution()
print(
    solution.findRelativeRanks(
        [10, 3, 8, 9, 4]
    )
)
