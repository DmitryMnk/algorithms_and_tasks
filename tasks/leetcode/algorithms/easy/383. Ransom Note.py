from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    c1 = Counter(ransomNote)
    c2 = Counter(magazine)
    print(c1, c2)

    for key, val in c1.items():
        if key not in c2:
            return False
        elif c2[key] < val:
            return False
    return True

print(
    canConstruct('aa', 'ab')
)