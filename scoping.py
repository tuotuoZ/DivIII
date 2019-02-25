import numpy as np

x = np.array([1, 2, 3])

def modify_test(x):

	x = x[0]
	return x

print(modify_test(x))
print(x)