# Write a NumPy program to split the element of a given array to multiple lines
import numpy as np
x = np.array(['2', '11', '234', '1234', '12345'], dtype=np.str)
print("\nOriginal Array:")
print(x)
r = np.char.zfill(x, 5)
print("\nNumeric string of 5 digits with zeros:")
print(r)