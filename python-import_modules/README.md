# Python - Import & Modules

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

* Why Python programming is awesome
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function dir()
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs

## Requirements

### General

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 22.04 LTS using python3 (version 3.10.*)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc

## Tasks

### 0. Import a simple function from a simple file

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition 1 + 2 = 3

* You have to use print function with string format to display integers
* You have to assign:
    * the value 1 to a variable called a
    * the value 2 to a variable called b
    * and use those two variables as arguments when calling the functions add and print
* a and b must be defined in 2 different lines: a = 1 and another b = 2
* Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
* You can only use the word add_0 once in your code
* You are not allowed to use * for importing or __import__
* Your code should not be executed when imported

### 1. My first toolbox!

Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

* Do not use the function print more than 4 times
* You have to define:
    * the value 10 to a variable a
    * the value 5 to a variable b
    * and use those two variables only, as arguments when calling functions
* Your program should call each of the imported functions
* The word calculator_1 should be used only once in your file
* You are not allowed to use * for importing or __import__
* Your code should not be executed when imported

### 2. How to make a script dynamic!

Write a program that prints the number of and the list of its arguments.

* The output should be:
    * Number of argument(s) followed by argument or arguments, followed by
    * : (or . if no arguments were passed) followed by
    * a new line, followed by (if at least one argument)
    * one line per argument:
        * the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
* Your code should not be executed when imported

### 3. Infinite addition

Write a program that prints the result of the addition of all arguments

* The output should be the result of the addition of all arguments, followed by a new line
* You can cast arguments into integers by using int()
* Your code should not be executed when imported

### 4. Who are you?

Write a program that prints all the names defined by the compiled module `hidden_4.pyc`

* You should print one name per line, in alpha order
* You should print only names that do not start with __
* Your code should not be executed when imported

### 5. Everything can be imported

Write a program that imports the variable a from the file `variable_load_5.py` and prints its value.

* You are not allowed to use * for importing or __import__
* Your code should not be executed when imported
