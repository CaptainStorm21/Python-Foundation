from functools import reduce



def accumulator (acc, item):
    reduce_list = [1, 2, 10, 9]
    print(acc, item)
    return acc + item

print (reduce( accumulator, reduce_list, 0))
# print(reduce_list)