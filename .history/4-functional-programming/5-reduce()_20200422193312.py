from functools import reduce



def accumulator (acc, item):
    print(acc, item)
    return acc + item

print (reduce( accumulator, reduce_list, 0))
# print(reduce_list)