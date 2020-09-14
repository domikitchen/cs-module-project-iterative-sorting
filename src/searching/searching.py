def linear_search(arr, target):
    count = 0
    for i in arr:
        if arr[count] == target:
            return count
        count += 1
    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        midpoint = (right + left) // 2

        if arr[midpoint] == target:
            return midpoint

        elif arr[midpoint] < target:
            left = midpoint + 1

        else:
            right = midpoint - 1
    return -1  # not found

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

print(binary_search(arr1, 98))