#!/usr/bin/python3
"""Initalize a function"""


def is_same_class(obj, a_class):
    """if object is an istance

    Args:
        obj: the object
        a_class: the class
    Returns:
        True or False
    """
    if (type(obj) == a_class):
        return True
    return False
