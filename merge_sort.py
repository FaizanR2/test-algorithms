import math


def mergesort(L):  # O(n log n)
    if len(L) < 2:
        return L

    mid_index = math.floor((len(L) / 2))
    left_arr = L[0: mid_index]
    right_arr = L[mid_index: len(L)]

    return merge(mergesort(left_arr), mergesort(right_arr))  # created a helper function named merge, O(n)


def merge(left_arr, right_arr):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            result.append(left_arr[left_index])
            left_index += 1

        else:
            result.append(right_arr[right_index])
            right_index += 1

    return result + left_arr[left_index:] + right_arr[right_index:]


L = [12, 3, 16, 6, 5, 1]

print(mergesort(L))

# example of a recursive function

# def f(n):
#     if n == 0: # base case
#         return
#     return f(n-1)  # function call until base case is satisfied
