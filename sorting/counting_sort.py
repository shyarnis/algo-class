# References:
#   CLRS 3e
#   https://www.programiz.com/dsa/counting-sort

def counting_sort(A):
    n = len(A)

    # C[0..k] count array or temporary working storage
    # initialize with zero upto k
    # C = [0] * k                  # IndexError: list index out of range
    C = [0] * 10
    
    # B[1..n] holds sorted output
    B = [0] * n

    for j in range(0, n):
        C[A[j]] += 1
    
    for i in range(1, 10):
        C[i] += C[i-1]

    for j in range(n-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    
    print(B)


if __name__ == "__main__":
    A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    counting_sort(A)
