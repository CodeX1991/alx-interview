#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data (list): the data set contain multiple characters

    Return:
        True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the first few bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1 byte char
            if num_bytes == 0:
                continue

            # UTF-8 character can be btween 2 and 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    # All char should be fully processed
    return num_bytes == 0
