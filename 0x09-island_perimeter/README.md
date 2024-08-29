Island Perimeter
Description
This project focuses on solving a geometric problem using a grid (2D array) representation of an island. The goal is to create a Python function that calculates the perimeter of an island, represented by connected land cells in a grid, where each cell can either be water (0) or land (1).

Requirements
Editors: vi, vim, emacs
OS: Ubuntu 20.04 LTS
Python Version: 3.4.3
Style Guide: PEP 8 (version 1.7)
No external libraries or modules are allowed
All files should be executable and end with a new line
The first line of all Python scripts should be #!/usr/bin/python3
The project directory must include a README.md file
Learning Objectives
Understanding and working with 2D arrays (matrices) in Python.
Applying conditional logic to determine the perimeter of land cells in a grid.
Developing counting techniques to calculate the perimeter based on adjacent cells.
Breaking down a problem into smaller tasks to solve it systematically.
Project Structure
The project consists of the following files:

bash
Copy code
0x09-island_perimeter/
│
├── 0-island_perimeter.py     # Python script with the island_perimeter function
├── 0-main.py                 # Test script to run the function with a sample grid
└── README.md                 # This documentation file
Function Description
island_perimeter(grid)
This function calculates the perimeter of an island described in the grid.

Parameters:

grid: A list of lists of integers, where:
0 represents water.
1 represents land.
Each cell is a square with a side length of 1.
Cells are connected horizontally/vertically, not diagonally.
The grid is rectangular, with width and height not exceeding 100.
The grid is completely surrounded by water, and there is only one island (no lakes).
Returns:

An integer representing the perimeter of the island.
Usage
You can test the function by running the provided 0-main.py script:

bash
Copy code
./0-main.py
Example output:

bash
Copy code
12
This output corresponds to the perimeter of the island in the sample grid provided.

Example
Given the following grid:

python
Copy code
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
The function island_perimeter(grid) will return 12, as the island perimeter is composed of 12 units.

Author
Victor Amajuoyi - hegavon
License
This project is licensed under the MIT License - see the LICENSE file for details.

