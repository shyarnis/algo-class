# Algorithm: Perform matrix addition of matrices A and B of row m and column n
# Time Complexity: O(n^2)

def mat_add(A, B, m, n):
    C = A
    for i in range(m):
        for j in range(n):
            C[i][j] += B[i][j]
    return C


# Input, 2D matrix as a list of list
mat_A = [[12, 52], [73, 47], [55, 36]]   # 3*2
mat_B = [[42, 32], [23, 42], [57, 10]]   # 3*2
rows = 3
columns = 2

# Output
print(mat_add(mat_A, mat_B, rows, columns))