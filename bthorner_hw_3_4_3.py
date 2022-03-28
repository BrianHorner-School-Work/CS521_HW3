"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 3_4_3
This program prompts the user for a sentence and calculates the amount
of uppercase letters, lowercase letters, digits and punctuation.
"""
# Importing string in order to compare characters to string.punctuation
import string
from string import punctuation as string_punctuation

# Grabbing user sentence
user_sentence_input = input("Please enter a sentence.")

# Establishing empty lists for each catagory of character
sentence_uppercase = []
sentence_lowercase = []
sentence_digits = []
sentence_punctuation = []

# For loop to go through user input sentence with for statement
for char in user_sentence_input:
    # Comparing character to string.punctuation, if match adding to list
    if char in string_punctuation:
        sentence_punctuation.append(char)
    # Checking if character is uppercase, if so appending to list
    elif char.isupper():
        sentence_uppercase.append(char)
    # Checking if character is lowercase, if so appending to list
    elif char.islower():
        sentence_lowercase.append(char)
    # Checking if character is a digit, if so appending to list
    elif char.isdigit():
        sentence_digits.append(char)
    # Else statement and pass for any irregularlity that do not fit
    else:
        pass
# Establishing lists in lists (array) for printing in correct format
character_print_output = [["# Upper", "# Lower", "# Digits", "# Punct."], ["--------", "--------", "--------", "--------"], [len(sentence_uppercase), len(sentence_lowercase), len(sentence_digits), len(sentence_punctuation)]]
# Printing for element in array. Each list has four printable items.
for i in character_print_output:
    # This makes each printed item centered with 8 padding between
    print("{:^8} {:^8} {:^8} {:^8}".format(*i))
