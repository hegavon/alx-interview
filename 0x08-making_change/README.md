0x08. Making Change
Project Overview
This project focuses on solving the classic coin change problem using algorithms such as dynamic programming and greedy algorithms. The goal is to determine the fewest number of coins needed to make a given amount using a specified set of coin denominations.

This problem is a common challenge in the field of algorithms, often used to test one's understanding of dynamic programming and greedy strategies. The problem requires you to find the optimal way to make a total amount using the fewest number of coins possible, given an infinite supply of coins of different denominations.

Concepts
Greedy Algorithms
Greedy algorithms work by making the locally optimal choice at each step, hoping to find the global optimum. While they can be useful, they don't always produce the optimal solution for the coin change problem.
Dynamic Programming
Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly useful for optimization problems where overlapping subproblems and optimal substructure are involved.
The dynamic programming approach ensures that the solution is both optimal and efficient.
Algorithmic Complexity
Understanding the time and space complexity of the algorithm is crucial for solving the problem within acceptable limits.
Requirements
General
Allowed editors: vi, vim, emacs
Environment: Ubuntu 20.04 LTS
Python Version: Python 3.4.3
Style: Your code should follow the PEP 8 style (version 1.7.x).
Executable Files: All your Python files must be executable.
README.md: A README file at the root of the project directory is mandatory.
First Line: All your files should start with #!/usr/bin/python3.
Problem Statement
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

Function Prototype
python
Copy code
def makeChange(coins, total):
Function Details
Parameters:
coins: A list of integers representing the denominations of the coins you have.
total: An integer representing the total amount to be made.
Return:
The fewest number of coins needed to meet the total.
Return 0 if the total is 0 or less.
Return -1 if the total cannot be met by any combination of coins in the list.
Constraints
The value of each coin will always be an integer greater than 0.
You can assume you have an infinite number of each denomination of coin in the list.
The solution's runtime will be evaluated for performance.
Example Usage
Input
python
Copy code
coins = [1, 2, 25]
total = 37
Output
Copy code
7
Explanation
The fewest number of coins needed to make 37 using the coins [1, 2, 25] is 7. The optimal solution would be 1 coin of 25, 1 coin of 10 (2x5), and 2 coins of 1.

Input
python
Copy code
coins = [1256, 54, 48, 16, 102]
total = 1453
Output
diff
Copy code
-1
Explanation
It is not possible to make 1453 using the available coins.

Implementation
Dynamic Programming Approach
The dynamic programming approach involves creating a table to store the minimum number of coins needed to make each value from 0 to total. The table is filled in a bottom-up manner, ensuring that each subproblem is solved optimally.