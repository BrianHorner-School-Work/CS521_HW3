"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 3_4_2
This program takes an odd lengthed string and does a set of calclations.
"""
# Setting string constant
ODD_STRING = "The dog laid down peacefully and waited for her food."

# Calculating the len of the string
string_len = (len(ODD_STRING))
# Calculting the middle of the string
string_middle = int(string_len / 2)
# Putting string elements into list for indexing
odd_string_list = ODD_STRING.split()

# Checkign the make sure string is odd, if not printing error message
if string_len % 2 == 0:
    print("The string you entered \"{}\" is not an odd numbered string".format(ODD_STRING))
else:
    # Printing the length of the string and the string
    print("My {}-character string is: \"{}\"".format(string_len, ODD_STRING))
    # Printing the middle character of the string
    print("The middle character is: \"{}\"".format(ODD_STRING[string_middle]))
    # Printing the first half of the string excluding middle character
    print("The first half of the string is: \"{}\"".format(
        ODD_STRING[:string_middle]))
    # Printing the second half of the string excluding middle character
    print("The second half of the string is: \"{}\"".format(
        ODD_STRING[string_middle + 1:]))
