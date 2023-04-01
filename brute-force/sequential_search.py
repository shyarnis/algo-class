def sequential_search(A, K):
    i = 0
    n = len(A)
    while i<n and A[i]!=K:
        i=i+1
    if i<n:
        return i
    else:
        return -1
