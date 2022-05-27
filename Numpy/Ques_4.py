# Write a NumPy program to make the length of each element 15 of a given array and the string centered / left-justified / right-justified with paddings of _.
import numpy as np
x = np.array(['python exercises', 'PHP', 'java', 'C++'], dtype=np.str)
print("Original Array:")
print(x)
centered = np.char.center(x, 15, fillchar='_')
left = np.char.ljust(x, 15, fillchar='_')
right = np.char.rjust(x, 15, fillchar='_')
print("\nCentered =", centered)
print("Left =", left)
print("Right =", right)
