import cupy as cp

# float32 matrix
matrix = cp.random.rand(20000, 20000).astype("f")

# inverse
inverse_matrix = cp.linalg.inv(matrix)

print(inverse_matrix)
