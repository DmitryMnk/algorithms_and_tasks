class Solution:
    def findComplement(self, num: int) -> int:
        number = bin(num)[2:]
        flipped = ''

        for i in number:

            if i == '0':
                flipped += '1'
            else:
                flipped += '0'
        return int(flipped, 2)

solution = Solution()
print(solution.findComplement(5))