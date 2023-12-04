#!/usr/bin/env python3
def no_c(my_string):
    reef = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            reef += char
    return reef

