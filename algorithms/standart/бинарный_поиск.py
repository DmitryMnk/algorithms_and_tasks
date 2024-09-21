def binary_search(
    array: list,
    searching_elem: int
) -> int | None:
    left_limit = 0
    right_limit = len(array) - 1
    while left_limit <= right_limit:

        middle = (right_limit + left_limit) // 2
        print(left_limit, middle, right_limit)
        if array[middle] == searching_elem:
            return middle
        elif searching_elem > array[middle]:
            left_limit = middle + 1
        else:
            right_limit = middle - 1
    return None
