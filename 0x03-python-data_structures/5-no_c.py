#!/usr/bin/env python3
def no_c(my_string):
    reef = ''
    for u in range(len(my_string)):
        if (my_string[u] != 'c' and my_string[u] != 'C'):
            reef += my_string[u]
    return reef

