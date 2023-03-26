# Exercise 7.1-1
# Illustrate the operation of PARTITION on the array
# A = <13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11>

# One PARTITION
# pivot = 11

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
        print(A)
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


if __name__ == "__main__":
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    print(f"Before Partition => {A}")
    n = len(A)
    partition(A, 0, n-1)
    print(f"After Partition => {A}")    

    print(f"\nResult of one PARTITION where pivot element is {11}")