
def reverseVowels(s: str) -> str:
    alph = 'aeiouAEIOU'
    result = list(s)
    i = 0
    j = len(s) - 1

    print(result)
    while i <= j:
        if s[i] in alph and s[j] in alph:
            result[i] = s[j]
            result[j] = s[i]
            i += 1
            j -= 1
        else:
            if s[i] not in alph:
                i += 1
            if s[j] not in alph:
                j -= 1

    return ''.join(result)

print(reverseVowels(' '))