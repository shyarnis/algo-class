from typing import List
Array = List[int]

def selection_sort(A: Array) -> Array:
    n: int = len(A)

    for i in range(n-1):
        m: int = i

        for j in range(i+1, n):
            if A[j] < A[m]:
                m = j
        
        A[i], A[m] = A[m], A[i]

    return A

if __name__ == "__main__":
    array = [4, 23, 1, 54, 16, 82, 80, 93, 42, 22]
    print(selection_sort(A=array))