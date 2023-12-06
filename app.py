import numpy as np
"""
Ex17:
arr = np.ones([5, 5])
newarr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
print(newarr)

Ex18:
print("0 * np.nan:", 0 * np.nan)
print("np.nan == np.nan:", np.nan == np.nan)
print("np.inf > np.nan:", np.inf > np.nan)
print("np.nan - np.nan:", np.nan - np.nan)
print("np.nan in set([np.nan]):", np.nan in set([np.nan]))
print("0.3 == 3 * 0.1:", 0.3 == 3 * 0.1)


Ex19:
matrix = np.arange(9).reshape(3, 3)
diagonal_values = np.diag(matrix)
print(diagonal_values)



Ex20:
matrix = np.ones((8, 8))

matrix[::2, ::2] = 0  # Even rows, even columns
matrix[1::2, 1::2] = 0  # Odd rows, odd columns
matrix[::2, 1::2] = 1  # Even rows, odd columns
matrix[1::2, ::2] = 1 # Odd rows, even columns
print(matrix)

"""