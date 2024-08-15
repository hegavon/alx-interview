# 0. Rotate 2D Matrix

## Project Overview

This project focuses on implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. The challenge emphasizes understanding matrix manipulation and in-place operations in Python, aiming to enhance algorithmic thinking and problem-solving skills.

## Key Concepts

- **Matrix Representation in Python**: Utilizing lists of lists to represent 2D matrices and manipulating their elements.
- **In-place Operations**: Modifying the matrix without creating copies, minimizing space complexity.
- **Matrix Transposition**: Swapping rows and columns as part of the rotation process.
- **Reversing Rows**: Manipulating matrix rows by reversing their order to achieve the desired rotation.
- **Nested Loops**: Using nested loops to iterate through 2D data structures effectively.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.10).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the project is mandatory.
- Code should adhere to the `pycodestyle` style (version 2.8.0).
- No modules are allowed to be imported.
- All modules and functions must be documented.
- All files must be executable.

## Implementation

### Task 0: Rotate 2D Matrix

**Prototype**: `def rotate_2d_matrix(matrix):`

This function takes a 2D matrix as input and rotates it 90 degrees clockwise in-place. The matrix will have 2 dimensions and will not be empty.

### Example Usage

Here is an example of how to use the `rotate_2d_matrix` function:

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Resources
Python Official Documentation
GeeksforGeeks Articles
TutorialsPoint

Conclusion
By completing this project, you will gain hands-on experience with matrix manipulation and deepen your understanding of in-place operations, which are crucial in optimizing algorithms and data structures.