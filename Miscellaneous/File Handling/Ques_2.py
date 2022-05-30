#Write a program in python to read first 5 characters from the file(“data.txt”)?
f = open("data.txt","r")
l = f.read(5)
print(l)