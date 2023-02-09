# Algorithm: Perform matrix addition of matrices A and B of row m and column n
# Time Complexity: O(n^2)

def mat_add(A, B, m, n):
    C = [[0, 0, 0], [0, 0, 0]]
    for i in range(m):
        for j in range(n):
            # C[i,j] = A[i,j] + B[i,j]
            C[i][j] = A[i][j] + B[i][j]
    return C


# Input, 2D matrix as a list of list
mat_A = [[12, 52, 73], [47, 55, 36]]   # 2*3
mat_B = [[11, 22, 33], [34, 25, 36]]   # 2*3
rows = 2
columns = 3

# Output
print(mat_add(mat_A, mat_B, rows, columns))
