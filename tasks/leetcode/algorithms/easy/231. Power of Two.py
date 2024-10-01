def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False

    step = 0

    while True:
        result = 2 ** step
        if result == n:
            return True
        elif result > n:
            return False
        step += 1


print(is_power_of_two(18))