#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        value = my_list[0]
        for item in range(len(my_list)):
            if my_list[item] > value:
                value = my_list[item]
        return value
