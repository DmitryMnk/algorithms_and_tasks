def length_of_last_word(s: str) -> int:
    words = s.split()
    return len(words[-1])


print(length_of_last_word(
    'luffy is still joyboy'
))