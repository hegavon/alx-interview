#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """Returns a list of lists of numbers representing the Pascal's triangle"""
    if n <= 0:
        return []

    pascal_triangle = []

    for i in range(n):
        # Define a row and fill first and last indices with 1
        new_row = [0] * (i + 1)
        new_row[0] = 1
        new_row[-1] = 1

        for j in range(1, i):
            if j < len(new_row):
                a = get_value_or_zero(pascal_triangle[i - 1], j)
                b = get_value_or_zero(pascal_triangle[i - 1], j - 1)
                new_row[j] = a + b

        pascal_triangle.append(new_row)

    return pascal_triangle


def get_value_or_zero(row, index):
    if index < len(row):
        return row[index]
    else:
        return 0
