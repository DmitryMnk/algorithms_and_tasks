from typing import List


def array_rank_transform(arr: List[int]) -> List[int]:
    ranks = sorted(list(set(arr)))

    r_dict = {value: rank + 1 for rank, value in enumerate(ranks)}

    answer = [r_dict[val] for val in arr]

    return answer

print(
    array_rank_transform(
    [37,12,28,9,100,56,80,5,12]
    )
)