"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 3_6_5
This program takes an 20 word sentence from an input file and prints 5
words per a line on an output file
"""


# Importing os module and os.path from os module
import os
from os import path
# define contstant variables for ma word counter, line word count
# & word count
MAX_WORD_COUNT = 20
LINE_WORD_COUNT = 5
WORD_COUNTER = 0
# Establishing empty strings for use in conversions
input_sentence = ""
output = ""

# Testing to see if input file exists
if path.exists("bthorner_hw_3_6_5_input.txt"):
    # Opening the input file in read and the output file in write
    input_file = open("bthorner_hw_3_6_5_input.txt", "r")
    output_file = open("bthorner_hw_3_6_5_output.text", "w")
    # Cleaning up input string from input file
    input_sentence = input_file.read()
    input_sentence = input_sentence.split()
    # Printing error message if sentence in input has more than 20 words
    if len(input_sentence) == MAX_WORD_COUNT:
        for word in input_sentence:
            if WORD_COUNTER < LINE_WORD_COUNT or len(output) <= LINE_WORD_COUNT:
                # Adding word to output string
                output = output + word + " "
                # Increasing word counter
                WORD_COUNTER += 1
            # Writing sentence to file at word counter or len limit
            elif len(output) == 5 or WORD_COUNTER == LINE_WORD_COUNT:
                # Stripping to get rid of an inconsistant white space
                output_file.write(output.strip())
                output_file.write("\n")
                # Resetting ouput sentence and word counter
                output = " "
                WORD_COUNTER = 0

        # Closing the files
        input_file.close()
        output_file.close()

    else:
        # Error message if there are more than 20 words in sentence
        print("Error you have {} words in your sentence. You need to have"
              " 20 words.".format(
                  len(input_sentence)))
# Printing error if input file does not exist
else:
    print("Error: Input file does not exist. Please fix error.")
