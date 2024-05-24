#!/usr/bin/python3
"""declaration of function"""


def append_write(filename="", text=""):
    """write into a file

    Args:
        filename: the name of the file.
        text: the text we want.

    Returns:
        the number of characters.
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
