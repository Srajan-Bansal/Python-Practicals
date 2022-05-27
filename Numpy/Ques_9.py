# Write a NumPy program to split the element of a given array with spaces.
import numpy as np
x = np.array(['Python\Exercises, Practice, Solution'], dtype=np.str)
print("Original Array:")
print(x)
r = np.char.splitlines(x)
print(r)
