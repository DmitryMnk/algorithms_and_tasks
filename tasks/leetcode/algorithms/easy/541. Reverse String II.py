class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        count_s = 0
        count_blocks = 0
        substr = ''
        for i in s:
            substr += i
            count_s += 1
            if count_s == k:
                if count_blocks % 2 == 0:
                    result += substr[::-1]
                else:
                    result += substr
                substr = ''
                count_s = 0
                count_blocks += 1
        print(count_blocks)
        if count_blocks % 2 == 0:
            return result + substr[::-1]
        return result + substr

solutions = Solution()
print(solutions.reverseStr(
    'hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl',
    39
))
