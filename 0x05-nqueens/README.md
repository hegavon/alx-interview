0x05. N Queens
Summary
The N Queens project is a classic algorithm problem that involves placing N queens on an N×N chessboard such that no two queens threaten each other. This project primarily requires an understanding of backtracking algorithms and recursion to solve efficiently.

Key Concepts and Resources
Backtracking Algorithms
Understanding Backtracking: Backtracking is a systematic way to iterate through all the possible configurations of a search space. When a solution fails, the algorithm backtracks to the previous step and tries a different path.
Introduction to Backtracking: Backtracking Introduction
Recursion
Recursion in Python: Using recursive functions is crucial for implementing the backtracking algorithm in this problem.
Recursion Tutorial: Recursion in Python
List Manipulations in Python
Creating and Manipulating Lists: You'll need to manipulate lists to keep track of the positions of queens on the board.
Python Lists Documentation: Python Lists
Python Command Line Arguments
Handling Command-Line Arguments: The program should handle command-line arguments using the sys module.
Command Line Arguments Tutorial: Command Line Arguments in Python
Project Requirements
General Requirements:
Use allowed editors: vi, vim, emacs
Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All files should end with a new line
The first line of all files should be #!/usr/bin/python3
A README.md file is mandatory
Code should follow PEP 8 style (version 1.7.*)
All files must be executable
Task Description
0. N Queens

Write a program that solves the N queens problem.

Usage: nqueens N
If the user calls the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1.
Where N must be an integer greater or equal to 4.
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1.
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1.
The program should print every possible solution to the problem.
One solution per line in the format: see example.
Solutions do not have to be printed in a specific order.
Only the sys module is allowed for import.