#!/usr/bin/python3
def no_c(my_string):
    _return = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            _return += my_string[i]
    return _return
