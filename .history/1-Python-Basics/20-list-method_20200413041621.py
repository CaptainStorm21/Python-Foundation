basket = [21, 12,33, 35, 99]
print(basket)

print(len(basket))

#33 gets pops because it is 2nd number in the array
print(basket.pop(2))
print(basket)

#extend
basket1 = [1000, 2000, 3000]
print(basket.extend(basket1))
print(basket)

#append - last to the list
print(basket.append(700))
print(basket)

#index
print(basket.index(21))
print(basket)
basket.sort()
print(basket)


#insert
print(basket.insert(3, 'new'))
print(basket)



#look up
forest = ['trees', 'bush', 'mushrooms', 'berries' ]
#false
print ('x' in forest)
#true
print ('trees' in forest)

#true
print ('i' in 'I love forest rain')

#1
print (forest.count('trees'))


