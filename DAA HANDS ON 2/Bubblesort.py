def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test Case 1: Random array
arr1 = [23, 36, 25, 2, 22, 15, 86]
print("Sorted array 1:", bubble_sort(arr1))

# Test Case 2: Already sorted array
arr2 = [11, 12, 13, 14, 15]
print("Sorted array 2:", bubble_sort(arr2))

# Test Case 3: Reverse sorted array
arr3 = [15, 14, 13, 12, 11]
print("Sorted array 3:", bubble_sort(arr3))

# Test Case 4: Array with all identical elements
arr4 = [8, 8, 8, 8, 8]
print("Sorted array 4:", bubble_sort(arr4))

# Test Case 5: Array with negative numbers
arr5 = [-35, -2, 9, -54, 10]
print("Sorted array 5:", bubble_sort(arr5))
