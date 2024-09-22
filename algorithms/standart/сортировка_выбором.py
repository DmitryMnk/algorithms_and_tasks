def selection_sort(array_for_sort):

    for k in range(len(array_for_sort) - 1):
        swap_index = k
        for i in range(k + 1, len(array_for_sort)):
            if array_for_sort[i] < array_for_sort[swap_index]:
                swap_index = i
        array_for_sort[k], array_for_sort[swap_index] = array_for_sort[swap_index], array_for_sort[k]

    return array_for_sort
