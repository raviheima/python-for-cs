# Write a program that generates a random number, x, between 1 and 50, a random number
# y between 2 and 5, and computes x to the power of  y

import random

x = random.randint(1,50)
y = random.randint(2,5)
compute = x ** y
print(f"X:{x} to the power of Y:{y} = {compute}")