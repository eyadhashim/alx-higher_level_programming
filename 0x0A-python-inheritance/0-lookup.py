#!/usr/bin/python3
"""function return the list of available attributes
    """


def lookup(obj):
    """the function

    Args:
        obj: the obj we want it attributes
    """
    return (dir(obj))
