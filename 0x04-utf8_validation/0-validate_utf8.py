#!/usr/bin/python3
"""
Function to determine if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding
    Args:
        data (list of int): the data set to check
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for byte in data:
        # Get the binary representation of the byte and keep the last 8 bits
        bin_rep = format(byte, '#010b')[-8:]

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            for bit in bin_rep:
                if bit == '0':
                    break
                num_bytes += 1

            # 1-byte character (0xxxxxxx)
            if num_bytes == 0:
                continue

            # Invalid scenarios according to UTF-8 encoding rules
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Continuation bytes must start with '10'
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0


# Example usage:
if __name__ == "__main__":
    data1 = [65]
    data2 = [
        80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33
    ]
    data3 = [229, 65, 127, 256]

    print(validUTF8(data1))  # Expected output: True
    print(validUTF8(data2))  # Expected output: True
    print(validUTF8(data3))  # Expected output: False
