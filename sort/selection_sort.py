def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        min = i
        # find minimum in unsorted sublist
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        # swap
        A[i], A[min] = A[min], A[i]
    return A

# input
input_array = [5, 4, 3, 2, 1]

# ouput
print(selection_sort(input_array))



