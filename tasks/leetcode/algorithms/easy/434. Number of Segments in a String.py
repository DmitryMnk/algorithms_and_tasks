def countSegments(s: str) -> int:
    # count = 0
    # is_symbol = False
    # for i in s:
    #     if i != ' ':
    #         is_symbol = True
    #     else:
    #         if is_symbol:
    #             count += 1
    #             is_symbol = False
    #
    # if is_symbol:
    #     count += 1
    #
    # return count

    return len(s.split())

print(
    countSegments(
        "Hello"
    )
)