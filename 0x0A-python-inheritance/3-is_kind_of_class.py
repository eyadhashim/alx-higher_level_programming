#!/usr/bin/python3
"""Function"""


def is_kind_of_class(obj, a_class):
    """is the object is an instance

    Args:
        obj: the object
        a_class: the class
    Returns:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
