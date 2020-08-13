#!/opt/anaconda3/bin Python

from functools import reduce

my_list = [1, 2, 3, 4]

# Approach without mapreduce - loop over it
ssv_trad = sum([i ** 2 for i in my_list])

squared_values = map(lambda i: i ** 2, my_list)


def add_numbers(x1, x2):
    return x1 + x2


ssv_mapreduce = reduce(add_numbers, squared_values)

print('trad ' + str(ssv_trad))
print('map-reduce ' + str(ssv_mapreduce))
