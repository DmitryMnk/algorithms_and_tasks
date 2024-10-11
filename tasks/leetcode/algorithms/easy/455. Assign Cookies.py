from typing import List


def findContentChildren(g: List[int], s: List[int]) -> int:
    if not s:
        return 0
    i, j = 0, 0
    count = 0
    s = sorted(s)
    g = sorted(g)
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1

    return count

print(
    findContentChildren(
[1, 2], [1, 2, 3]
    )
)

