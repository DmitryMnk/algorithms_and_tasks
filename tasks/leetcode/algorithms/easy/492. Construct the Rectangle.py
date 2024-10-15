from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area == 1:
            return [1, 1]

        minimal = float('inf')
        result = [0, 0]
        for i in range(1, area // 2 + 1):
            width = i
            length = area / i
            if length.is_integer() and length >= width:
                if length - width < minimal:
                    result[0] = int(length)
                    result[1] = width

        return result

solution = Solution()

print(solution.constructRectangle(10))
