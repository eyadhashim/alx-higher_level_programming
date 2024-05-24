#!/usr/bin/python3
"""Declaration of function"""
import json


def save_to_json_file(my_obj, filename):
    """Returns an object represented by a JSON

    Args:
        my_obj: the object
        filename: the name of file
    """
    with open(filename, "w") as my_file:
        json.dump(my_obj, my_file)
