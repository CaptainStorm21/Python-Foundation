# lambda expressions
from functools import reduce

my_list = [2, 4, 6, 8]

print(my_list)
print(list(map(lambda item: item * 2, my_list)))