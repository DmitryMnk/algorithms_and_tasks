


def convertToTitle(columnNumber: int) -> str:
    if columnNumber <= 26:
        return chr(ord('A') + columnNumber - 1)

    result= ''
    while columnNumber > 0:

        step = columnNumber % 26
        if step == 0:
            step = 26
            columnNumber -= 1
        result =  chr(ord('A') + step - 1) + result
        columnNumber //= 26

    return result
print(
    convertToTitle(701)
)