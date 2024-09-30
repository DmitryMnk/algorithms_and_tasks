
def is_happy(n: int) -> bool:
    count = 0
    visited = set()
    while n != 1:
        visited.add(n)
        count += 1
        result = 0
        while n > 0:
            result += (n % 10) ** 2
            n //=10
        n = result
        if n in visited:
            return False
    return True

print(is_happy(2))