def isBadVersion(version):
    return version >= 2

def first_bad_version(n: int) -> int:

    if n == 1:
        return 1

    left = 1
    right = n

    while left <= right:
        middle = (left + right) // 2
        print(left, right)
        prev = isBadVersion(middle - 1)
        result = isBadVersion(middle)

        if result and not prev:
            return middle

        elif result:
            right = middle - 1
        elif not result:
            left  = middle + 1



print(first_bad_version(
    2
))