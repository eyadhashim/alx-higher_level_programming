#!/usr/bin/python3
"""Declaration of function"""
import json


def to_json_string(my_obj):
    """returns JSON representation

    Args:
        my_obj: the string

    Returns:
        the representation
    """
    return json.dumps(my_obj)
