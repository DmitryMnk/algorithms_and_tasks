def add_binary(a: str, b: str) -> str:
    i = len(a) - 1
    j = len(b) - 1
    result = ''
    carry = 0
    while i >= 0 or j >= 0:
        s = carry
        if i >= 0 and a[i] == '1':
            s += 1
        if j >= 0 and b[j] == '1':
            s += 1

        i -= 1
        j -= 1

        if s > 1:
            carry = 1
        else:
            carry = 0
        result = str(s % 2) + result

    if carry:
        result = '1' + result
    return result

print(
    add_binary(
        '1010',
        '1011'
    )
)