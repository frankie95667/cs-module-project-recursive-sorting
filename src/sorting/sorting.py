# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i = j = k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here\
    if(len(arr) <= 1):
        return arr
    midpoint = len(arr) // 2
    L = arr[:midpoint]
    R = arr[midpoint:]

    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L, R)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    elements = end
    merged_arr = [0] * elements
    i = start
    j = mid
    k = 0
    while i < mid and j < end:
        if arr[i] < arr[j]:
            merged_arr[k] = arr[i]
            i += 1
        else:
            merged_arr[k] = arr[j]
            j += 1
        k += 1
    while i < mid:
        merged_arr[k] = arr[i]
        i += 1
        k += 1
    while j < end:
        merged_arr[k] = arr[j]
        j += 1
        k += 1
    return merged_arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    print(str(l), str(r))
    if len(arr[l:r]) <= 1:
        return arr[l:r]
    mid = (r - l) // 2
    merge_sort_in_place(arr, l, mid)
    merge_sort_in_place(arr, mid + 1, r)

    return merge_in_place(arr, l, mid, r)

