# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [ 3, 23, 111, 3423, 352]
print(numbers)
print(type(numbers))

#using a constructor
listNum = list (( 213, 11, 342, 2342, 55432))
print(listNum)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
print(fruits[2])

#Get len
print(len(fruits))

#append to the list
fruits.append('Mango')
print(fruits)

#remove from the list
fruits.remove('Grapes')
print(fruits)

#insert into a spot
fruits.insert(2, 'Coconut')
print(fruits)

#remove from a spot
fruits.(2, 'Coconut')
print(fruits)