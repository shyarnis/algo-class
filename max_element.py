# Algorithm: To return maximum element from given input array A of size m
# Time Complexity: O(n)

def MAX(A, n):
    max_element = 0
    for i in range(n):
        if A[i] > max_element:
            max_element = A[i]
    return max_element

# Input
Array = [1, 34, 534, 53, 775, 23, 223, 33, 80, 90, 55]
size = 11

# Output
print(MAX(Array, size))