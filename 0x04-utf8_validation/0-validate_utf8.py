#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    nbytes = 0

    b1 = 1 << 7
    b2 = 1 << 6

    for i in data:
        b = 1 << 7
        if nbytes == 0:
            while b & i:
                nbytes += 1
                b = b >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (i & b1 and not (i & b2)):
                return False
        nbytes -= 1
    return nbytes == 0
