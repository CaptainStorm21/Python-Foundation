from functools import reduce

reduce_list = [1, 2, 3, 4]

def accumulator (acc, item):
    # print(acc, item)
    return acc + item



#print (reduce( accumulator, reduce_list, 0))
#starts at 0
# you can start with whatever number

print (reduce( accumulator, reduce_list, 10))
# print(reduce_list)

