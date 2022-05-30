#Write a Python program to calculate surface volume and area of a sphere?
pi=22/7
radian = float(input('Radius of sphere: '))
sur_area = 4 * pi * radian **2
volume = (4/3) * (pi * radian ** 3)
print("Surface Area is: ", sur_area)
print("Volume is: ", volume)