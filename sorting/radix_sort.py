# References:
#   CLRS 3e
#   https://www.programiz.com/dsa/radix-sort

def count_sort(A, digit):
    n = len(A)
    C = [0] * 10
    B = [0] * n

    for i in range(0, n):
        index = (A[i] // digit) % 10  
        C[index] += 1

    for i in range(1, 10):
        C[i] += C[i-1]
    
    for i in range(n-1, -1, -1):
        index = (A[i] // digit) % 10
        B[C[index]-1] = A[i]
        C[index] -= 1

    for i in range(n):
        A[i] = B[i]

def radix_sort(A):
    max_element = max(A)
    digit = 1
    while max_element // digit > 0:
        count_sort(A, digit)
        digit *= 10
    

if __name__ == "__main__":
    A = [612, 220, 542, 404, 103, 304, 104, 67, 111, 963, 9082, 54, 1114]
    radix_sort(A)
    print(A)
