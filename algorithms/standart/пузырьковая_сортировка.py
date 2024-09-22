def bubble_sort(array_for_sort):
    for i in range(1, len(array_for_sort)):
        is_sorted = True
        for k in range(len(array_for_sort) - i):
            if array_for_sort[k] > array_for_sort[k + 1]:
                is_sorted = False
                array_for_sort[k], array_for_sort[k + 1] = array_for_sort[k + 1], array_for_sort[k]
        if is_sorted:
            break

    return array_for_sort
