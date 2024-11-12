import cupy as cp
import numpy as np
import time

matrix = cp.random.rand(20000, 20000).astype("f")

start_time = time.time()

inverse_matrix = cp.linalg.inv(matrix)

end_time = time.time()
print(f"Cupy operation time: {end_time - start_time} seconds")


matrix = np.random.rand(20000, 20000).astype("f")

start_time = time.time()

inverse_matrix = np.linalg.inv(matrix)

end_time = time.time()
print(f"Numpy operation time: {end_time - start_time} seconds")