#!/usr/bin/python3


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

# Generate the Pascal's triangle up to the given number of rows
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

# Return the generated Pascal's triangle as a list of lists
    return triangle


# Test the function with a sample input
if __name__ == "__main__":
    n = 5
    for row in pascal_triangle(n):
        print(row)
