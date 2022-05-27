# Write a NumPy program to remove the trailing whitespaces of all the elements of a given array.
import numpy as np
x = np.array(['Python PHP Java C++'], dtype=np.str)
print("Original Array:")
print(x)
r = np.char.split(x)
print("\nSplit the element of the said array with spaces: ")
print(r)
