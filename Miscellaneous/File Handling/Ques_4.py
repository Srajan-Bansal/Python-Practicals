#Write a program in python to display number of lines in a file(“data.txt”)?
f = open("data.txt",'r')
L = f.readlines()
print(len(L))