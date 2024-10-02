def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(words) != len(pattern):
        return False

    table_s = {}
    table_w = {}

    for i in range(len(words)):
        char = pattern[i]
        word = words[i]

        if char not in table_s:
            table_s[char] = word

        if word not in table_w:
            table_w[word] = char

        if table_w[word] != char or table_s[char] != word:
            return False
    return True


print(word_pattern(
    "abba",
    'cat dog dog eat'
))