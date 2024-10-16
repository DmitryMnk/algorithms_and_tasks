from collections import Counter


def repeatedSubstringPattern(s: str) -> bool:

    print((s+s)[1:-1])

    return True if s in (s+s)[1:-1] else False


print(
    repeatedSubstringPattern(
        'abcab'
    )
)


