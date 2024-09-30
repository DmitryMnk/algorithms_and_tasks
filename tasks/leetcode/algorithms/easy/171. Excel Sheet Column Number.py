def title_to_number(columnTitle: str) -> int:
    col = 1
    k = len(columnTitle) - 1
    for i in columnTitle[:-1]:
        index = ord(i) - ord('A') + 1
        col += index * 26 ** k
        k -= 1
    col += ord(columnTitle[-1]) - ord('A')
    return col

print(title_to_number('AB'))