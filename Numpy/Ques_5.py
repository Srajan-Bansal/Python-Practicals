# Write a NumPy program to encode all the elements of a given array in cp500 and decode it again.
import numpy as np
x = np.array([' python exercises ', ' PHP  ', ' java  ', '  C++'], dtype=np.str)
print("Original Array:")
print(x)
stripped = np.char.strip(x)
print("\nRemove the leading and trailing whitespaces: ", stripped)