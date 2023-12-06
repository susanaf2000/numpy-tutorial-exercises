import numpy as np

print(np.__version__)
x = np.zeros(10)
print(x)
print(x.size)
print(x.itemsize)
total_memory_size = x.size * x.itemsize
print(total_memory_size)
print(np.info(np.add))