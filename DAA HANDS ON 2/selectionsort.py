def selection_sort(data):
    length = len(data)
    for current_index in range(length):
        # Assume the minimum is the current index
        min_index = current_index
        # Compare against the elements after the current index to find the smallest
        for compare_index in range(current_index + 1, length):
            if data[compare_index] < data[min_index]:
                min_index = compare_index
        # Swap the found minimum element with the element at the current index
        data[current_index], data[min_index] = data[min_index], data[current_index]
    return data

# Test Case 1: List with random integers
test_case_1 = [45, 3, 12, 7, 29]
print("Sorted Test Case 1:", selection_sort(test_case_1))

# Test Case 2: List with elements already in ascending order
test_case_2 = [1, 2, 3, 4, 5]
print("Sorted Test Case 2:", selection_sort(test_case_2))

# Test Case 3: List with elements in descending order
test_case_3 = [9, 8, 7, 6, 5]
print("Sorted Test Case 3:", selection_sort(test_case_3))

# Test Case 4: List with all identical elements
test_case_4 = [4, 4, 4, 4]
print("Sorted Test Case 4:", selection_sort(test_case_4))

# Test Case 5: List with a mix of positive and negative numbers
test_case_5 = [-5, 2, -1, 7, 0]
print("Sorted Test Case 5:", selection_sort(test_case_5))
