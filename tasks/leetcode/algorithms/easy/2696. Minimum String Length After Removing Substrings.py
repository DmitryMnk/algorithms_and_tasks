def min_length(s: str) -> int:
    # while 'AB' in s or 'CD' in s:
    #     s = s.replace('AB', '')
    #     s = s.replace('CD', '')
    # return len(s)

    stack = []
    s = list(s)
    for c in s:
        if not stack:
            stack.append(c)
        else:
            if (c == "B" and stack[-1] == "A") or (c == "D" and stack[-1] == "C"):
                stack.pop()
            else:
                stack.append(c)
    return len(stack)

print(min_length(
"ACBBD"
))