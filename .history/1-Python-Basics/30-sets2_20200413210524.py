# methods
my_set = { 342, 23, 1,  2,  3,  9,  10,  9 }
your_set = [ 342, 23, 42, 46, 53, 34, 10 ]
print(my_set)

#output {1, 2, 3, 9}
print(my_set.difference(your_set))

#output {1, 2, 3, 9, 342, 23}
my_set.discard(10)
print(my_set)

#output {1, 2, 3, 9, 342, 23}
my_set.intersection(your_set)
print(my_set)

#
my_set1 = { 342, 23, 1,  2,  3,  9,  10,  9 }
my_set1.isdisjoint(your_set)
print(my_set)