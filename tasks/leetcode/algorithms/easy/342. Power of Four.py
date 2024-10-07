import math


def isPowerOfFour(n: int) -> bool:
    # if n <= 0:
    #     return False
    # while n % 4 == 0:
    #     n //= 4
    #
    # return n == 1
    c = 1
    while c < n:
        c = c << 2
    return c == n
print(isPowerOfFour(4))