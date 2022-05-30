#Write a program to sum all the values of a dictionary.
dict={'key 1':100,'key 2':300}
x=[]
for i in dict.values():
    x.append(i)
print(sum(x))