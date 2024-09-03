def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        # Test against elements after i to find the smallest
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Test Case 1: Random array
arr1 = [9, 17, 4, 87, 14]
print("Sorted array 1:", selection_sort(arr1))

# Test Case 2: Already sorted array
arr2 = [11, 12, 13, 14, 15]
print("Sorted array 2:", selection_sort(arr2))

# Test Case 3: Reverse sorted array
arr3 = [15, 14, 13, 12, 11]
print("Sorted array 3:", selection_sort(arr3))

# Test Case 4: Array with all identical elements
arr4 = [9, 9, 9, 9, 9]
print("Sorted array 4:", selection_sort(arr4))

# Test Case 5: Array with negative numbers
arr5 = [-8, -1, 4, -9, 80]
print("Sorted array 5:", selection_sort(arr5))
