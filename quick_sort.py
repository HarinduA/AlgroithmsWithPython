def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]     # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]    # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [33, 10, 59, 26, 41, 58, 18]
sorted_arr = quick_sort(arr)
print("Sorted array is:", sorted_arr)
