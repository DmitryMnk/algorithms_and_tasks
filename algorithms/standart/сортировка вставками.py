def insertion_sort(array_for_sort):
    for i in range(len(array_for_sort)):
        for k in range(len(array_for_sort) - i - 1):
            if array_for_sort[k] > array_for_sort[k + 1]:
                array_for_sort[k], array_for_sort[k + 1] = array_for_sort[k + 1], array_for_sort[k]
    return array_for_sort
