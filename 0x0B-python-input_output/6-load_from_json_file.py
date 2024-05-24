#!/usr/bin/python3
"""Declaration of function"""
import json


def load_from_json_file(filename):
    """Returns an object represented by a JSON

    Args:
        filename: the name of file
    Returns:
        the load of JSON
    """
    with open(filename) as my_file:
        return json.load(my_file)
