from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = 'qwertyuiop'
        second = 'asdfghjkl'
        third = 'zxcvbnm'
        row = 0

        result = []

        for word in words:
            s_row = 0
            is_it = True
            for s in word.lower():
                if s in first:
                    row = 1
                elif s in second:
                    row = 2
                else:
                    row = 3
                if row != s_row and s_row != 0:
                    is_it = False
                else:
                    s_row = row
            if is_it:
                result.append(word)

        return result

slution = Solution()

print(
    slution(["Hello","Alaska","Dad","Peace"])
)
