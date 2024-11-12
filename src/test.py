import cupy as cp

# float64 matrix
matrix = cp.random.rand(20000, 20000).astype("float64")

# inverse
inverse_matrix = cp.linalg.inv(matrix)

print(inverse_matrix)
