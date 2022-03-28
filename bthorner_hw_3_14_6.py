"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 3_14_6
This program reads student data by line from an input files and stores
the individual student data in a list and stores all student lists into another master student list
"""

# Importing os and path to determine if file exists at its location
import os
from os import path

# Establishing student and students lists
individual_student_list = []
all_students_list = []

# Testing to make sure input file exists
if path.exists("bthorner_hw_3_14_6_input.txt"):
    # open input file
    input_file = open("bthorner_hw_3_14_6_input.txt", "r")
# Iterating through file lines
    for lines in input_file:
        # Splitting lines with no whitespace and storing in individual lists.
        individual_student_list = lines.strip().splitlines()
# Storing the student list in master list
        all_students_list.append(individual_student_list)
# Printing master list with Name of student, student ID, and GPA highlighted
    print("Here is the student data with Name of the Student, Student ID, and  GPA respectively:\n {}".format(
        all_students_list))
# Closing input file
    input_file.close()
else:
    # Checking to make sure input file exists
    print("Error: File does not exist in specified file path.")
