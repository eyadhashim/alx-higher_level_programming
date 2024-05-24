#!/usr/bin/python3
"""Declaration to function"""


def class_to_json(obj):
    """return dictionary description with simple data structure.

    Args:
        obj: is an instance of a Class

    Returns:
        dictionary
    """
    return obj.__dict__
