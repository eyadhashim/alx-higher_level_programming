#!/usr/bin/python3
"""declartion of function"""


def write_file(filename="", text=""):
    """write to file
    Args:
        filename: the name of the file
        text: the text we want to write into the file.
    Returns:
        the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
