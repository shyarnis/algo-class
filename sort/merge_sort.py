# Algorithm: Perform merge sort of given unsorteds list A
# Output: sorted list 
# Time Complexity: O(nlogn)

def merge_sort(A, p, r):
    if p < r:
        q = p+r//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)

        merge(A, p, q, r)

    return A


def merge(A, p, q, r):
    pass

# Input: An unsorted list A
A = [13, 42, 12, 43, 59, 90, 34]

# Output
print(merge_sort(A))