from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    answer = ''
    sorted_strs = sorted(strs)
    left = sorted_strs[0]
    right = sorted_strs[-1]
    for i in range(min(len(left), len(right))):
        if left[i] != right[i]:
            return answer
        answer += left[i]
    return answer

