def divide_and_sort(data):
    # Base condition: If the list has 0 or 1 element, it's already sorted
    if len(data) <= 1:
        return data

    # Find the middle point and split the list into two sublists
    mid_point = len(data) // 2
    left_part = data[:mid_point]
    right_part = data[mid_point:]

    print(f"Dividing: {data} -> {left_part} and {right_part}")

    # Recursively apply merge sort on both halves
    left_sorted = divide_and_sort(left_part)
    right_sorted = divide_and_sort(right_part)

    # Combine the sorted halves
    combined = merge_halves(left_sorted, right_sorted)
    print(f"Combining: {left_sorted} and {right_sorted} -> {combined}")
    return combined

def merge_halves(left, right):
    combined_list = []
    left_pointer = 0
    right_pointer = 0

    # Merge the two halves in ascending order
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            combined_list.append(left[left_pointer])
            left_pointer += 1
        else:
            combined_list.append(right[right_pointer])
            right_pointer += 1

    # Add any remaining elements from either left or right
    combined_list.extend(left[left_pointer:])
    combined_list.extend(right[right_pointer:])
    return combined_list

# Example test case using the same array
sample_array = [5, 2, 4, 7, 1, 3, 2, 6]
sorted_result = divide_and_sort(sample_array)
print(f"Sorted array: {sorted_result}")
