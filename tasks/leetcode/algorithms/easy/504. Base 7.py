class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        n = abs(num)
        result = ''
        while n > 0:
            result = str(n % 7) + result
            n //= 7

        if num < 0:
            result = '-' + result

        return result

solution = Solution()
print(
    solution.convertToBase7(-7)
)
