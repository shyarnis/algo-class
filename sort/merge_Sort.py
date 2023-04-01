def merge_sort(A, p, r):
    """Merge sort.

    Args:
        A: unsorted list
        p: first index
        r: last index

    Returns:
        Sorted list.
    """
    if p<r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
        return A

def merge(A, p, q, r):
    """Merge two sorted sublist.

    Args:
        A: unsorted list
        p: first index
        q: middle index
        r: last index
        
    Returns:
        Sorted sublist through merging.
    """
    n_1 = q-p+1             # length of A[p:q], left part
    n_2 = r-q               # length of A[q+1:r], right part
    
    # L[1..n_1+1] and R[1..n_2+1] be new arrays
    L = []
    R = []

    # copy of A[p:q] into L[1: n_1]
    for i in range(1, n_1):
        L[i] = A[p+i-1]
    
    # copy of A[q+1:r] into R[1: n_2]   
    for j in range(1, n_2):
        R[j] = A[q+j]
    
    i = 1
    j = 1
    for k in range(p, r):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i+1
        elif A[k] == R[j]:
            j = j+1

    


if __name__ == "__main__":
    arr = [43, 5, 39, 33, 90, 22, 30, 32, 44, 53]
    print(merge_sort(arr, 1, 9))