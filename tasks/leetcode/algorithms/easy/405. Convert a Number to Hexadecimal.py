def toHex(num: int) -> str:
    if num == 0:
        return "0"

    hex_chars = "0123456789abcdef"
    result = ''
    if num < 0:
        num = (1 << 32) + num

    while (num > 0):
        r = num % 16
        result = hex_chars[r] + result
        num = num // 16


    return result

