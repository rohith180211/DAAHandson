def partition_array(array, start, end):
    pivot_value = array[end]
    index = start - 1

    for j in range(start, end):
        if array[j] <= pivot_value:
            index += 1
            array[index], array[j] = array[j], array[index]

    array[index + 1], array[end] = array[end], array[index + 1]
    return index + 1

def select_kth_smallest(array, start, end, k):
    if start == end:
        return array[start]

    pivot_index = partition_array(array, start, end)
    left_size = pivot_index - start + 1  # Number of elements in the left partition

    if k == left_size:
        return array[pivot_index]
    elif k < left_size:
        return select_kth_smallest(array, start, pivot_index - 1, k)
    else:
        return select_kth_smallest(array, pivot_index + 1, end, k - left_size)


array = [10, 7, 8, 9, 1, 5]
k = 2  
kth_element = select_kth_smallest(array, 0, len(array) - 1, k)
print(f"The {k}nd smallest element is {kth_element}")
