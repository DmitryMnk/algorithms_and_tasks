from collections import Counter


def firstUniqChar(s: str) -> int:
    cnt = Counter(s)
    if len(cnt) == 1:
        return 0
    for i in range(len(s)):
        if cnt[s[i]] == 1:
            return i


print(
    firstUniqChar('loveleetcode')
)