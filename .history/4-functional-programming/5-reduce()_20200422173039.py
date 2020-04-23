from functools import reduce

reduce_list = [324, 232, 1, 2, 4, 6, 111, 99]

def accumulator (acc, item):
    return acc + item

print (reduce( accumulator, reduce_list, 0))
print(reduce_list)