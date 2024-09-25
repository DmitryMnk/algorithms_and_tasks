def str_str(haystack: str, needle: str) -> int:
    answer = -1
    count = 0
    if haystack == needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        print(haystack[i: i + len(needle)])
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1

print(
    str_str(
        haystack = "abc",
        needle = "c"
    )
)
s = 'a'
print(s[0: 1])