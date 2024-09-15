def remove_dups(arr):
    if not arr:
        return []

    # Index of the next unique element
    idx = 0

    # Traverse the array starting from the second element
    for i in range(1, len(arr)):
        if arr[i] != arr[idx]:
            idx += 1
            arr[idx] = arr[i]

    # Return the array up to the point where unique elements are stored
    return arr[:idx + 1]


# Example usage:
array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print(remove_dups(array1))
# Output: [2]

print(remove_dups(array2))
# Output: [1, 2, 3, 4, 5]
