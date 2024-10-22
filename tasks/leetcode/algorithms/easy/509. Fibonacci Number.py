
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
           return 0
        elif n == 1 or n == 2:
           return 1

        last = 1
        prelast = 1
        result = 0
        k = 3
        while k <= n:
           result = last + prelast
           prelast = last
           last = result
           k += 1
        return result

solution = Solution()
print(solution.fib(10))