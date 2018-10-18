#!/usr/bin/env python3

def reverse_string(string):
    if string == "":   # base case, when recursion reaches the end of string its going to be empty
        return ""
    sub_str = reverse_string(string[1:])  # get the last element or the sub sol of the string
    sub_sol = sub_str + string[0]
    return sub_sol

assert reverse_string("gaurav") == "varuag"

print(reverse_string("gaurav"))
