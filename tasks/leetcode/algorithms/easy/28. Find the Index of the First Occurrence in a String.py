def str_str(haystack: str, needle: str) -> int:
    if haystack == needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        print(haystack[i: i + len(needle)])
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1
