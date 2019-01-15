#
#simple python script to split a check
#

import math 

#define function split_check
def split_check(total, number_of_people):
    if number_of_people <= 1: #if its less than 1 person we raise an error
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_people) #math.ceil rounds up the result


try: #this is for the errorhandling in case a user types in words
    total_due = float(input("What is the total?  "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err: #here we print out the error
    print("Oh no! Thats no a valid value. Try again...")
    print("({})".format(err))
else: #here the output will be printed if no error occurs
    print("Each person owes ${}".format(amount_due))

############nicog99############nicog99############nicog99############nicog99############
