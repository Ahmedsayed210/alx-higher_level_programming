#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
  if tuple_a[0] == 0 or tuple_b[0] == 0:
    return (0, 0)
  else:
    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[0]
    return(first, second)
