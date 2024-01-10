#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary.keys())
        max = 0
        best_key = ""
        for key in keys:
            if a_dictionary[key] > max:
                max = a_dictionary[key]
                best_key = key
        return best_key
    else:
        return None
