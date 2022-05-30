# Write a Python program to generate a random alphabetical character, alphabetical string and alphabetical string of a fixed length.
importrandom
importstring
print("Generatearandomalphabeticalcharacter:")
print(random.choice(string.ascii_letters))
print("\nGeneratearandomalphabeticalstring:")
max_length=255
str1=""
foriinrange(random.randint(1,max_length)):
str1+=random.choice(string.ascii_letters)
print(str1)
print("\nGeneratearandomalphabeticalstringofafixedlength:")
str1=""
foriinrange(10):
str1+=random.choice(string.ascii_letters)
print(str1)