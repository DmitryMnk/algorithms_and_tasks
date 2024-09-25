def roman_to_int(s: str) -> int:

    translation = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    s = s.replace('IV', 'IIII')
    s = s.replace('IX', 'VIIII')
    s = s.replace('XL', 'XXXX')
    s = s.replace('XC', 'LXXXX')
    s = s.replace('CD', 'CCCC')
    s = s.replace('CM', 'DCCCC')

    result = 0
    for symbol in s:
        result += translation[symbol]
    return result

print(roman_to_int("MCMXCIV"))
