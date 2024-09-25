def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    str_num = str(x)
    return str_num[::-1] == str_num
