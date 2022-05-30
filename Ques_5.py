#Write a program in python to map 2 lists into a dictionary?
from multiprocessing.sharedctypes import Value
from optparse import Values


keys=[1,2,4]
Val=["VALUE1","VALUE2","VALUE3"]
dict=dict(zip(keys,Val))
print(dict)