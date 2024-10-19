class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # s = '0'
        # if n == 1:
        #     return s
        #
        # def rev_invert(s):
        #     res = ''
        #     for k in s:
        #         if k == '0':
        #             res += '1'
        #         else:
        #             res += '0'
        #     return res[::-1]
        #
        # c = 1
        # while c != n:
        #     s += '1' + rev_invert(s)
        #     c += 1
        # return s[k - 1]

        if n == 1:
            return '0'

        length = (1 << n) - 1
        mid = length // 2 + 1
        if k == mid:
            return '1'

        if k < mid:
            return self.findKthBit(n - 1, k)

        return '1' if self.findKthBit(n - 1, length - k + 1) == '0' else '0'

solution = Solution()
print(solution.findKthBit(
    4, 11
))