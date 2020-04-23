# lambda expressions  = anonomys functions in JS
from functools import reduce

my_list = [2, 4, 6, 8]


print(list(map(lambda item: item * 2, my_list)))
print(my_list)


print(list(filter(lambda item: item % 2 !=))