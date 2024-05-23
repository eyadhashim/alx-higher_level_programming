#!/usr/bin/python3
"""implement a new class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init method

        Args:
            width (int): the width
            height (int): the height
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area method"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ perimeter method
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """printable the rectangle with #
        return new list
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        my_list = []
        for i in range(self.__height):
            for j in range(self.__width):
                my_list.append(str(self.print_symbol))
            if i != self.__height - 1:
                my_list.append("\n")
        return ("".join(my_list))

    def __repr__(self):
        """Return string
        """
        my_list = "Rectangle(" + str(self.__width)
        my_list += ", " + str(self.__height) + ")"
        return (my_list)

    def __del__(self):
        """print a message
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the rectangle

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        Raises:

