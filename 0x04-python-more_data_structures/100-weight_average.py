#!/usr/bin/python3
def mul(tup=()):
    return (tup[0] * tup[1])


def weight_average(my_list=[]):
    sw = []  # <score><weight>
    total_weight = []
    if len(my_list) == 0:
        return 0
    for i in my_list:
        sw.append(mul(i))
        total_weight.append(i[1])
    return sum(sw) / sum(total_weight)
