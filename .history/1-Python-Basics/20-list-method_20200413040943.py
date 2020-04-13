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

print(basket.sort())


#insert
print(basket.insert(9000))
