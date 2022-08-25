# IntroToProg-Python-Mod07

Deja Monet

Randal Root

Foundations of Python

24 August 2022

## Assignment 07: Files & Exceptions

### Introduction

In this assignment, I will review Python exceptions or error handling and pickling. I will also review defining and calling custom errors as functions.

### Completing the Assignment: Researching Exception Handling

This assignment directed students to learn about exception handling and Pickling in Python. My first step was to research what exception handling was, and choose an appropriate script that demonstrated this issue.

The first resource I used to research exception handling was w3schools.com. This resource showed that exceptions can be handled using the try statement (**Figure 1**).

![image](https://user-images.githubusercontent.com/111031988/186559303-009b91cb-e5ea-494f-b1cc-9fed477718df.png)
*Figure 1: A description of Exception Handling from w3schools.com*

I then checked geeksforgeeks.org to see more examples of exception handling (**Figure 2**).

![image](https://user-images.githubusercontent.com/111031988/186568152-c6e117a5-a3cd-4747-9a31-e1252bb79513.png)
*Figure 2. An example of Exception Handling from geeksforgeeks.org*

From these two resources, I learned that a script can be written to catch built-in Python exceptions, or a programmer can create their own custom exceptions. I decided that to demonstrate error handling, I would write a script that performed as a basic calculator. In order to elevate this script from the previous assignment in this course in which we used basic mathematical operations, I decided I would use classes and functions in order to retrieve the user’s input, process data, and define custom errors.

### Completing the Assignment: Writing a Script

I began by defining the mathematical operators add, subtract, multiply, and divide as strings, then defined a function to retrieve the user’s first number, choice of mathematical operator, and second number as the function **retrieve_user_input**. This function returns the user’s input so that they can be used in other functions (**Figure 3**).

![image](https://user-images.githubusercontent.com/111031988/186568345-6eccb719-7658-4743-b46f-3c6b79ae748a.png)
*Figure 3. The mathematical operators are defined, and user input is retrieved in a function.*

I decided that potential errors from the user input could be if the user did not enter a mathematical operation when prompted, or did not enter a number when prompted. I defined the class **errors** and created the functions **no_operation()** and **no_numeric()** to capture these respective issues (**Figure 4**).

![image](https://user-images.githubusercontent.com/111031988/186568519-ae3f03fb-e994-4528-b4eb-ebad26a62725.png)
*Figure 4. Custom errors are raised if the user does not enter the correct input when prompted.*

I then defined a **processing** class that completes the mathematical operation as chosen by the user, with each mathematical operation defined as its own function. The **divide** function has the potential to raise the **ZeroDivisionError** exception, in which the user is alerted that they cannot divide by zero (**Figure 5**).

![image](https://user-images.githubusercontent.com/111031988/186568630-122defb8-a634-4669-940d-074cd00e0397.png)
*Figure 5. The ZeroDivisionError exception is raised if the user attempts to divide by zero.*
