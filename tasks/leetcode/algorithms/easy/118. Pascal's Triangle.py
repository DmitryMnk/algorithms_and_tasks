from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 1:
        return [[1]]
    result = [[1]]
    for i in range(1, numRows):
        prev_item = result[i - 1]
        new_item = [1]
        for j in range(1, len(prev_item)):
            number = prev_item[j - 1] + prev_item[j]
            new_item.append(number)
        new_item.append(1)
        result.append(new_item)
    return result

print(generate(6))
