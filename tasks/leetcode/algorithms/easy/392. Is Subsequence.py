from collections import deque
from inspect import stack


def isSubsequence(s: str, t: str) -> bool:
    if s == '' and t != '':
        return True
    elif s == '' and t == '':
        return False

    stack = deque()

    for i in range(1, len(s)):
        stack.append(s[i])
    first_s = s[0]
    for j in t:
        if first_s == j and not stack:
            return True
        elif first_s == j:
            first_s = stack.popleft()
    return False

print(
    isSubsequence(
    "axc",
    "ahbgdc"
    )
)
