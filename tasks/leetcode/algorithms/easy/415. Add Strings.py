def addStrings(num1: str, num2: str) -> str:

    result = ''
    ost = 0

    i = len(num1) - 1
    j = len(num2) - 1

    while i >= 0 or j >= 0:
        if i >= 0 and j >= 0:
            a = int(num1[i]) + int(num2[j]) + ost

        elif i >= 0:
            a = int(num1[i]) + ost

        elif j >= 0:
            a = int(num2[j]) + ost

        result = str(a % 10) + result
        ost = a // 10
        i -= 1
        j -= 1

    if ost != 0:
        result = str(ost) + result

    return result

print(
    addStrings(
        '99', '99'
    )
)