#!/usr/bin/python3
"""Declaration of function"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON

    Args:
        my_str: the string

    Returns:
        an object
    """
    return json.loads(my_str)
