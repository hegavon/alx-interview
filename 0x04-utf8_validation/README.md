0x04. UTF-8 Validation
Description
This project focuses on validating whether a given dataset represents a valid UTF-8 encoding. The UTF-8 encoding scheme is widely used for encoding characters in a way that is both efficient and compatible with ASCII. This project will test your understanding of bitwise operations, the UTF-8 encoding scheme, and Python programming skills.

Requirements
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3).
All files should end with a new line.
The first line of all your files should be exactly #!/usr/bin/python3.
Your code should use the PEP 8 style (version 1.7.x).
All files must be executable.
A README.md file, at the root of the folder of the project, is mandatory.
Concepts
Bitwise Operations in Python
Understanding how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), and shifts (<<, >>).

UTF-8 Encoding Scheme
Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
Understanding the patterns that represent a valid UTF-8 encoded character.
Data Representation
How to represent and work with data at the byte level.

List Manipulation in Python
Iterating through lists, accessing list elements, and understanding list comprehensions.

Boolean Logic
Applying logical operations to make decisions within the program.

Task
0. UTF-8 Validation
Write a method that determines if a given dataset represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False.
A character in UTF-8 can be 1 to 4 bytes long.
The dataset can contain multiple characters.
The data will be represented by a list of integers.
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.