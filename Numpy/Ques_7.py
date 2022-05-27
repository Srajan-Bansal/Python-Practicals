# Write a NumPy program to remove the leading whitespaces of all the elements of a given array.
import numpy as np
x = np.array([' python exercises ', ' PHP  ', ' java  ', '  C++'], dtype=np.str)
print("Original Array:")
print(x)
rstripped_char = np.char.rstrip(x)
print("\nRemove the trailing whitespaces : ", rstripped_char)