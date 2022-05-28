#  Define a function which counts vowels and consonant ina word.
def count(val):
 vov = 0
 con = 0
 for i in range(len(val)):
 if val[i] in ['a','e','i','o','u']:
 vov = vov+1
 else:
 con = con + 1
 print("Count of vowels is ",vov)
 print("Count of consonant is ",con)
x = input("Enter Value: ")