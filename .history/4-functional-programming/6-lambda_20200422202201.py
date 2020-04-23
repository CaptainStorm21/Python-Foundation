# lambda expressions  = anonomys functions in JS
from functools import reduce

my_list = [2, 4, 6, 8, 99, 81]

print('original')
print(my_list)
print('post multiplication')
print(list(map(lambda item: item * 2, my_list)))


print('filter lambda')
print(list(filter(lambda item: item % 2 !=0, my_list)))

print('reduce')
print(reduce(lambda item: item % 2 !=0, my_list)))