#!/usr/bin/python3
"""Initalize a MyList class"""


class MyList(list):
    """MyList class

    Args:
        list: super class
    """
    def print_sorted(self):
        """print the list
        """
        print(sorted(self))
