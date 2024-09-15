import heapq

def merge_sorted(arrays):
    heap = []
    result = []

    # Initialize the heap with the first element from each array
    for i, arr in enumerate(arrays):
        if arr:  # Ensure the array is not empty
            heapq.heappush(heap, (arr[0], i, 0))  # (value, array index, element index)

    # Continue extracting the smallest element and adding the next element from the same array
    while heap:
        value, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(value)

        # If there's a next element in the same array, push it into the heap
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))

    return result


# Example usage:
arrays1 = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
]
arrays2 = [
    [1, 3, 7],
    [2, 4, 8],
    [9, 10, 11]
]

print(merge_sorted(arrays1))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(merge_sorted(arrays2))
# Output: [1, 2, 3, 4, 7, 8, 9, 10, 11]
