"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 3_4_4
This program takes a user input and make sure it is a number,
is 3 digits, and makes sure they are in ascending order, and has no duplicate
numbers
"""

""" This function will put digits or digits depending on how many over
or under the users input is from the ideal value. """


def missing_digits(digits):
    if digits == 1:
        return "digit"
    elif digits > 1:
        return "digits"


# Grabbing user input
input_number = input("Please enter a 3-digit integer: ")

# Defining variable value for loop
X = 1
# Creating loop in which the program will rely on
while X < 2:
    # Checking to see if input is a number
    if input_number.isnumeric():
        # Checking to see if 3 numbers were entered. Would be just characters if we did not check the input to see if it was numbers before
        if len(input_number) == 3:
            if (input_number[0] != input_number[1]) and (input_number[0] != input_number[2]) and (input_number[1] != input_number[2]):
                # Checking to make sure number is ascending
                if ((int(input_number[0])) < int(input_number[1]) and int(input_number[2])) and ((int(input_number[1])) < (int(input_number[2]))):
                    # Printing an accepted statement to user
                    print("Your number {} has been accepted. Congratulations!".format(input_number))
                    # Ending loop once number has been accepted
                    X += 1
                else:
                    # Error statement for not being ascending
                    print("Error: Your number {} is not in ascending order.".format(input_number))
                    # Prompting user for new number
                    input_number = input("Please enter a 3-digit integer: ")
            # Error statement for digits of number not being unique
            elif (input_number[0] == input_number[1]) or (input_number[0] == input_number[2]) or (input_number[1] == input_number[2]):
                print("Error: Your number {} contains duplication".format(input_number))
                # Prompting user for new number
                input_number = input("Please enter a 3-digit integer: ")
# Error for number not being 3 digits with greater or less than functionality
        elif len(input_number) < 3:
            input_short = abs(len(input_number) - 3)
            # These print statements use the digits function
            print("Error: Your number {0} is not 3-digits. It is missing {1} {2}.".format(input_number, input_short, missing_digits(input_short)))
            input_number = input("Please enter a 3-digit integer: ")
        elif len(input_number) > 3:
            input_over = len(input_number) - 3
            # Uses digit function
            print("Error: your number {0} is not 3 digits. It has {1} extra {2}.".format(input_number, input_over, missing_digits(input_over)))
            input_number = input("Please enter a 3-digit integer: ")
    # Error message if number is not an integer
    else:
        print("Error: Your input {} is not an integer.".format(input_number))
        input_number = input("Please enter a 3-digit integer: ")
