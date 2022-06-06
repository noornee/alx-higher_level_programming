#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = ()
    if len(tuple_b) < 2:
        tuple_b = (*tuple_b, 0)
    if len(tuple_a) < 2:
        tuple_a = (*tuple_a, 0)
    for a, b in zip(tuple_a, tuple_b):
        sum = (*sum, a + b)
    return sum
 
tuple_a = (1, 89)
# print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

