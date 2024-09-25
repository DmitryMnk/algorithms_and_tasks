from collections import deque

def is_valid( s: str) -> bool:

    if len(s) <= 1:
        return False

    pares = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    q = deque()
    for bracket in s:
        if bracket in pares.keys():
            q.append(bracket)
        else:
            if len(q) == 0:
                return False

            if pares[q[-1]] == bracket:
                q.pop()
            else:
                return False
    if len(q) != 0:
        return False
    return True

print(
    is_valid('(]')
)