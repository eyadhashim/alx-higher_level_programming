#!/usr/bin/python3
"""Pascal Tringle"""


def pascal_triangle(n):
    """The main function of pascal triangle"""
    if n <= 0:
        return []

    pa_tring = [[1]]

    while len(pa_tring) != n:
        tringle = pa_tring[-1]
        tmp = [1]
        for index in range(len(tringle) - 1):
            tmp.append(tringle[index] + tringle[index + 1])
        tmp.append(1)
        pa_tring.append(tmp)
    return pa_tring
