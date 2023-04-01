def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-1-i):
            if A[j+1] < A[j]:
                A[j+1], A[j] = A[j], A[j+1]
    return A

if __name__ == "__main__":
    array = [4, 23, 1, 54, 16, 82, 80, 93, 42, 22]
    print(bubble_sort(A=array))