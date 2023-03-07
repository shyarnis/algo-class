def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        min = i
        # find minimum element in unsorted list (right tira)
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        
        # swapping
        A[i], A[min] = A[min], A[i]
    
    return A

if __name__ == "__main__":
    arr = [43, 5, 39, 33, 90, 22, 30, 32, 44, 53]
    print(selection_sort(arr))