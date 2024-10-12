class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x > 0 or y > 0:
            b1 = x & 1
            b2 = y & 1
            if b1 != b2:
                count += 1
            x  = x >> 1
            y = y >> 1
        return count

print(bin(6), bin(1))
solution = Solution()
print(solution.hammingDistance(6, 1))
