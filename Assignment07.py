# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: This assignment is a calculator that returns 
#              messages when certain built-in Exceptions or defined errors are
#              triggered by user input.
# dejam,220823,Created and edited script
# ---------------------------------------------------------------------------- #

import sys
import pickle

#define mathematical operators
add = "+"
subtract = "-"
multiply = "*"
divide = "/"

#retrieve and return user input numbers and mathematical operator
def retrieve_user_input():
    print("Use two numbers and one operation!")
    first_number_input = float(input("Enter a first number: "))
    operation_input = input("""Enter one of the operations below:
                            + is addition
                            - is subtraction
                            * is multiplication
                            / is division 
                            """)
    second_number_input = float(input("Enter a second number: "))    
    return first_number_input, operation_input, second_number_input

class errors():
    #exits script if the user does not enter a mathematical operation when prompted
    @staticmethod
    def no_operation():
        print("Error: You must choose one mathematical operation! Exit script!")
        sys.exit()
    #exits script if the user does not enter a number when prompted
    @staticmethod
    def no_numeric():
        print("Error: You must enter numbers with your mathematical operation! Exit script!")
        sys.exit()
   
class processing():
    @staticmethod
    #return value if user chooses to add
    def add(first_number_input, second_number_input):
        variable_addition = first_number_input+second_number_input
        return variable_addition
    
    #return value if user chooses to subtract
    @staticmethod
    def subtract(first_number_input, second_number_input):
        variable_subtraction = first_number_input-second_number_input
        return variable_subtraction
    
    #return value if user chooses to multiply
    @staticmethod
    def multiply(first_number_input, second_number_input):
        variable_multiplication = first_number_input*second_number_input
        return variable_multiplication
    
    #return value if user chooses to divide
    #call exception if user attempts to divide by zero
    @staticmethod
    def divide(first_number_input, second_number_input):
        try:
            variable_division = first_number_input/second_number_input
        except ZeroDivisionError:
            print("Exception ZeroDivisionError: You cannot divide by zero!")
        return variable_division
    
    #complete mathematical operation or alert user a mathematical operation was not chosen
    @staticmethod
    def operation(first_number_input, operation_input, second_number_input):
        if add is operation_input:
            processed_number = processing.add(first_number_input, second_number_input)
            return processed_number
        if subtract is operation_input:
            processed_number = processing.subtract(first_number_input, second_number_input)
            return processed_number
        if multiply is operation_input:
            processed_number = processing.multiplication(first_number_input, second_number_input)
            return processed_number
        if divide is operation_input:
            processed_number = processing.divide(first_number_input, second_number_input)
            return processed_number
        else:
            errors.no_operation()
    
    #return processed number
    @staticmethod
    def return_value(processed_number):
        print("Your number is: " + str(processed_number))

#retrieve user input, call exception if user does not enter numbers when prompted
try:
    first_number_input, operation_input, second_number_input = retrieve_user_input()
except ValueError:
    print("Exception ValueError: You must enter a number!")

#print processed number if successfully processed, or alert user that there was a problem
try:
    processed_number = processing.operation(first_number_input, operation_input, second_number_input)
    processing.return_value(processed_number)
    
    #store processed number in a .dat file
    objFile = open("ProcessedNumber.dat", "ab")
    pickle.dump(processed_number, objFile)
    objFile.close()  
     
except NameError:
    print("Exception NameError: Something went wrong with the user input!")