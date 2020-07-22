# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    midpoint = start + ((end - start) // 2)
    if midpoint < 0:
        return -1

    if arr[midpoint] == target:
        return midpoint
    elif arr[midpoint] < target:
        return binary_search(arr, target, midpoint, end)
    else:
        return binary_search(arr, target, start, midpoint)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

