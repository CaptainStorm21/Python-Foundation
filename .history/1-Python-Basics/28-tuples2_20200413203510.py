#Tuples part 2

my_tuple = (2,  1, 4, 10, 34, 11, 342, 3242, 9000)
print(my_tuple)
new_tuple = my_tuple[1:10]
print(new_tuple)

x,y,z, *other = (2,  1, 4, 10, 34, 11, 342, 3242, 9000)
print (other)