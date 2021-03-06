# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
 
#  # simple tuple
# fruitTuple = ('Apple', 'Orange', 'Mango')
# print(fruitTuple)


# using a constructor
# fruitTuple1 = tuple(('Blueberry", ''Apple', 'Orange', 'Mango'))
# print(fruitTuple1)
# #Get a single value
# print(fruitTuple1[3])

# Cannnot change value
# fruitTuple1[3] = 'Pineapple'
# print(fruitTuple1)

# Tuples with one value should trailing comma
# fruit_tuple_2 = ('Apple')
# print(fruit_tuple_2)
# fruit_tuple_3 = ('Apple',)
# print(fruit_tuple_3)

# del  fruit_tuple_2
# print(fruit_tuple_2)

# Get length of tuple
# print(len(fruit_tuple_2))

# A Set is a collection which is unordered and unindexed. No duplicate members.
fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}
print(fruit_set)

# Add to the set 
fruit_set.add('StarFruit')
print(fruit_set)

# Remove to the set 
fruit_set.remove('StarFruit')
print(fruit_set)

#clear the set
fruit_set.clear()
print(fruit_set)

#delete set
del print(fruit_set)