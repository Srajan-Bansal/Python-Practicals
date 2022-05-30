# Write a Python program to construct a seeded random number generator, also generate a float between 0 and 1, excluding 1.
importrandom
print("Constructaseededrandomnumbergenerator:")
print(random.Random().random())
print(random.Random(0).random())
print("\nGenerateafloatbetween0and1,excluding1:")
print(random.random())