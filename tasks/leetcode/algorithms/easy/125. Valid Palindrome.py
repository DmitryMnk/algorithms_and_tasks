from operator import truediv


def is_palindrome(s: str) -> bool:
    alphabet = 'abcdefghjklmnopqrstuvwxyz'
    word = ''
    for i in s:
        if i.lower() in alphabet:
            word += i.lower()

    if word == word[::-1]:
        return True
    return False

print(
    is_palindrome(
        "race a car"
    )
)
