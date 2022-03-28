"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 3_2_1
This program evaluates a set range of numbers and determines how many
odd, even, perfect cube and perfect squares there are.
"""
# Establishing the number lists to be used to store the values
odd_numbers = []
even_numbers = []
square_numbers = []
cube_numbers = []

# Setting the start and end numbers to be used in the range
X_START = 2
X_END = 130

# Using the range function to count through the numbers and check them.
for i in range(X_START, X_END + 1):
    if i % 2 == 0:
        even_numbers.append(i)
    elif i % 2 == 1:
        odd_numbers.append(i)
    if round((i) ** (1 / 3)) ** 3 == (i):
        cube_numbers.append(i)
    if round((i) ** (1 / 2)) ** 2 == (i):
        square_numbers.append(i)

# Calculating the len of each list to find totals for each catagory.
total_cube = len(cube_numbers)
total_square = len(square_numbers)
total_even = len(even_numbers)
total_odd = len(odd_numbers)

# Printing results
print("Checkings numbers from {} to {} \n".format(X_START, X_END))
print("Odd ({}): {}...{}".format(
    total_odd, odd_numbers[0], odd_numbers[-1]))
print("Even ({}): {}...{}".format(
    total_even, even_numbers[0], even_numbers[-1]))
print("Square ({}): {}".format(total_square, square_numbers))
print("Cube ({}): {}".format(total_cube, cube_numbers))
