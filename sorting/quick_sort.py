def partition(A, p, r):
    x = A[r]
    i = p-1
    # for j in range(p, r-1):       # won't sort lowest element
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
        
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


if __name__ == "__main__":
    arr = [43, 5, 39, 33, 90, 22, 30, 32, 44, 53]
    n = len(arr)
    quick_sort(arr, 0, n-1)
    print(arr)
