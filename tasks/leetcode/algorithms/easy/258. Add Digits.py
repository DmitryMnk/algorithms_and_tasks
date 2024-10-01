def add(num: int) -> int:
    if num // 10 == 0:
        return num

    # def worker(number):
    #     result = 0
    #     while number > 0:
    #         result += number % 10
    #         number //= 10
    #     if result // 10 == 0:
    #         return result
    #     return worker(result)
    #
    # return worker(num)

    def worker(number):
        result = 0
        for s in str(number):
            result += int(s)
        if result < 10:
            return result
        return worker(result)

    return worker(num)
print(add(99))
