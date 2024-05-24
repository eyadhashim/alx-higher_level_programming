#!/usr/bin/python3
"""Class"""


class BaseGeometry:
    """Base Geometry class"""
    def area(self):
        """area instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator

        Args:
            name: name of variable
            value: the value of it

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than or equal 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
