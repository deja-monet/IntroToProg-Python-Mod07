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

The processing class also contains an **operation** function, which calls the mathematical operation function that the user chose. This function also returns an error message if the user did not choose a mathematical operation when prompted (**Figure 6**).

![image](https://user-images.githubusercontent.com/111031988/186568773-76203595-1602-4ac5-8d0a-967127e4a762.png)
*Figure 6. The operation function calls the mathematical operation that the user chose, or returns an error message.*

The processing class contains one final function that returns the processed number if the user entered two numbers and a mathematical operation correctly when prompted (**Figure 7**).

![image](https://user-images.githubusercontent.com/111031988/186568832-ea6311d6-d8a9-4eba-bc5a-8073901f4d40.png)
*Figure 7. The processed number is returned to the user.*

I then added two **try/except** statements in order to retrieve the user input and to process the user input. The first of these returns a message if a **ValueError** exception is raised, if the user does not enter a number when prompted. The second of these returns a message if a **NameError** exception is raised, and gives a general statement that there was a problem with the user input (**Figure 8**).

![image](https://user-images.githubusercontent.com/111031988/186568955-112849d1-6dd7-48a4-b640-28a0fe1b0b11.png)
*Figure 8. Try/Except statements that return error messages if specific conditions are met.*

With the research for exception handling completed and a script written that demonstrated this, I moved on to researching pickling.

### Completing the Assignment: Researching Pickling

The first resource I checked was geeksforgeeks.org. I learned that pickle is a module in Python that is used to serialize an object before it is written to a file (**Figure 9**).

![image](https://user-images.githubusercontent.com/111031988/186569057-4507ddd5-839a-437d-ac4e-133e343593b6.png)
*Figure 9. A description of Pickling from geeksforgeeks.org.*

I thought that I understood Pickling from reading the geeksforgeeks.org article, so I did not research any additional websites on this topic. In order to demonstrate Pickling in my script, I would need to import the pickle module and then write an object to a file using the pickle module.

### Completing the Assignment: Editing the Script

In order to demonstrate pickling in my script, I first imported the pickle module using **import pickle**. I decided that I would edit the last **try/except** statement such that if the user input was successfully processed, this output would be written to a .dat file (**Figure 10**).

![image](https://user-images.githubusercontent.com/111031988/186569186-1fa0b131-1748-41bb-a80a-92c9f8790e80.png)
*Figure 10. The processed number is written to a .dat file using the pickle module.*

With the script demonstrating both error handling and pickling, the script was completed, and it was time to begin testing the script in an IDE and Anaconda Prompt.

### Completing the Assignment: Testing the Script

I wrote this script in Spyder, and thus decided to use Spyder as my IDE for testing the script. The script prompts the user for a first number, a mathematical operation, and then a second number. I began by entering an acceptable input: 1+2. The script correctly returned the answer as 3.0. I then entered “a” as my second number, and the script correctly returned a ValueError and NameError exception (**Figure 11**).

![image](https://user-images.githubusercontent.com/111031988/186569313-51115b74-ddf7-4b70-bedb-1ac6913e1340.png)
*Figure 11. Testing the script in Spyder.*

I then needed to test the script in Anaconda Prompt. In Anaconda Prompt, I set the working directory to the correct location, then called the script using python. I decided to enter 1 as the first number, operation, and second number, and the script correctly returned one of my custom errors, as there was no operation entered. I then entered 10/0, and the script correctly returned the **ZeroDivisionError** and **NameError** (**Figure 12**).

![image](https://user-images.githubusercontent.com/111031988/186569379-848ace82-240c-4614-baf0-e92e5cc88721.png)
*Figure 12. Testing the script in Anaconda Prompt.*

Then, in Anaconda Prompt, I entered 3+2, and the script correctly returned 5.0. I then checked to see if a .dat file had been written to the working directory, and found that this had also been successful (**Figure 13**).

![image](https://user-images.githubusercontent.com/111031988/186569440-3ea88db7-ad15-4450-ac5f-696db2cb62be.png)
*Figure 13. The ProcessedNumber.dat file in the working directory.*

With the script able to demonstrate error handling, pickling, and tested in an IDE and Anaconda Prompt, the assignment was complete.

### Summary

In this assignment, I reviewed errors and error handling and writing serialized data using the pickle module. I also reviewed printing custom messages when built-in Python Exceptions are triggered in a script.



