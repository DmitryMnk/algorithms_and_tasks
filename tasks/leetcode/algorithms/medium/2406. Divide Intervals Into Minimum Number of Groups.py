from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        end_ptr, group_count = 0, 0

        print(start_times, end_times)

        for start in start_times:
            if start > end_times[end_ptr]:
                end_ptr += 1
            else:
                group_count += 1

        return group_count



ar = [[5,10],[6,8],[1,5],[2,3],[1,10]]
solution = Solution()
print(solution.minGroups(ar))