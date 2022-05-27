# Write a NumPy program to remove the leading and trailing whitespaces of all the elements of a given array.
import numpy as np
x = np.array([' python exercises ', ' PHP  ', ' java  ', '  C++'], dtype=np.str)
print("Original Array:")
print(x)
lstripped_char = np.char.lstrip(x)
print("\nRemove the leading whitespaces : ", lstripped_char)
