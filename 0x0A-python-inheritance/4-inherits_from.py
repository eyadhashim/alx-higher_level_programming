#!/usr/bin/python3
"""Function"""


def inherits_from(obj, a_class):
    """is the object is an instance

    Args:
        obj: the object
        a_class: the class
    Returns:
        True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
