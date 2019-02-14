# Practise NEA Task 5 v1.1
## by Mikey Herbert

## Stage 1: Analysis:

**What is the task asking me to do?**

* Make a program that can:
    * Log in
    * Register
    * Recover passwords
    * Provide security through encryption
* I will use these skills:
    * Sequence, selection and iteration
    * Variable handling
    * File handling
    * Object-oriented programming
    * Tkinter UI library
    * Subroutines
    * String manipulation
    * Datatype manipulation
    * Arrays
    * Flag variables

## Stage 2: Plan:

It is hard to show objects in a flowchart, so I will outline my thought processes here:
    
* 1st thing to do is import the required modules
* Next, I need to set up the App class and it's __init__ function:
    * Contains:
        * Object definitions (e.g. self.op1 and self.intro)
        * Initialisation commands
* Next, I need to set up the widgets for tthe menu window, so I'll do this in the create_widgets()
* After that, I need to set up the login(), register(), sub_register(), encode(), decode() and recovery() functions.
* The encoding works like this:
    * Takes the character
    * Converts it to ASCII number
    * Adds the length of the ciphertext and then 3 more. (or removes if it is decoding)
    * Converts the ASCII back to a character.
    * Returns the appropriate string
* Finally, I had to set up the geometry and set the trigger at the bottom.

## Stage 3: Code:
**Code is in the repository**

##Stage 4: Testing:

* I tested each of the functions with these tests:
    * login:
        * username invalid: fails
        * password invaild: fails
        * username + password for different accounts: fails
        * all correct: success
    * register:
        * passwords do not match: fails
        * all correct: success
    * recovery:
        * no match: fails
        * match: success

## Stage 5: Evaluation:

I think this program works well and I feel I have developed my skills as a programmer by implementing a UI and OOP.
