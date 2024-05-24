#!/usr/bin/python3
"""declaration of function"""


def read_file(filename=""):
    """read content of file

    Args:
        filename: the name of file.
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
