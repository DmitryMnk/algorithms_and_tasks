from collections import Counter


def longestPalindrome(s: str) -> int:

    cnt = Counter(s)
    length = 0
    max_k = 0
    for val in cnt.values():
        if val % 2 == 0:
            length += val
            print(val)
        else:
            if val > max_k:
                if max_k != 0:
                    length += (max_k - 1)
                max_k = val
            else:
                length += (val - 1)
    print(max_k, length)
    return length + max_k

print(
    longestPalindrome(
"abccccdd"
    )
)