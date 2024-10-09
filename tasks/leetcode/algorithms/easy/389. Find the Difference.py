from collections import Counter


def findTheDifference(s: str, t: str) -> str:
    cnt_s = Counter(s)
    cnt_t = Counter(t)

    for key, val in cnt_t.items():
        if key not in cnt_s:
            return key
        elif cnt_s[key] != val:
            return key

print(
    findTheDifference(
    "abcd",
    "abcde"
    )
)