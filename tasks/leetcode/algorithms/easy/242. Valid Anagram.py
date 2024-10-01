def is_anagram(s: str, t: str) -> bool:
    # if len(s) != len(t):
    #     return False
    #
    # s_table = {}
    # t_table = {}
    #
    # for i in range(len(s)):
    #     s_table.setdefault(s[i], 0)
    #     s_table[s[i]] += 1
    #
    #     t_table.setdefault(t[i], 0)
    #     t_table[t[i]] += 1
    # if t_table != s_table:
    #     return False
    # return True
    from collections import Counter
    c1 = Counter(s)
    c2 = Counter(t)
    if c1 == c2:
        return True
    return False

print(is_anagram(
    "rat", "car"
))