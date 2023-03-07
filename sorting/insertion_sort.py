def insertion_sort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j-1

        # i>0 won't sort A[1] index
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    
    return A

if __name__ == "__main__":
    arr = [43, 5, 39, 33, 90, 22, 30, 32, 44, 53]
    print(insertion_sort(arr))