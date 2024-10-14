class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        string = ''
        result = ''
        for i in s:
            if i != '-':
                string += i

        length = len(string)

        if length % k == 0:
            count = 1
            for i in range(length):
                if count == k and i != length - 1:
                    result += string[i] + '-'
                    count = 1
                else:
                    result += string[i]
                    count += 1
        else:
            result = string[:length % k]
            if length > k:
                result += '-'
            count = 1
            for i in range(length % k, length):
                if count == k and i != length - 1:
                    result += string[i] + '-'
                    count = 1
                else:
                    result += string[i]
                    count += 1
        return result.upper()

solution = Solution()
print(solution.licenseKeyFormatting("2-5g-3-J", 2))