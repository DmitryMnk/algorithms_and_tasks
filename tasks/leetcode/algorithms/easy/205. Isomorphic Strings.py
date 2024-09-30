def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    table_s = dict()
    table_t = dict()
    # for i in range(len(s)):
    #     table_s.setdefault(s[i], set())
    #     table_s[s[i]].add(t[i])
    #
    #     table_t.setdefault(t[i], set())
    #     table_t[t[i]].add(s[i])
    #
    # s_values = list(table_s.values())
    # t_values = list(table_t.values())
    # if len(s_values) != len(t_values):
    #     return False
    # for i in range(len(s_values)):
    #     if len(s_values[i]) > 1 or len(t_values[i]) > 1:
    #         return False
    # return True

    for i in range(len(s)):
        s_s = s[i]
        t_s = t[i]

        if s_s not in table_s:
            table_s[s_s] = t_s

        if t_s not in table_t:
            table_t[t_s] = s_s

        if table_s[s_s] != t_s or table_t[t_s] != s_s:
            return False
    return True

print(
    is_isomorphic('pager', 'title')
)
