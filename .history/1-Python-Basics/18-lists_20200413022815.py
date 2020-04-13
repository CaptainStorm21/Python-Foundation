# creating a list 
li = [1,2,3,4,5]
li2 = ['a', 'b', 'c', 'd']
li3 = [10, 23, 11, 'x', 'y', 'z', True]

print(li3[1])

# list slicing 
amazon_phones = [
    'Nokia',
    'Sharp',
    'Sony',
    'Samsung',
    'HTC',
    'Microsoft',
    'Panasonic'
]

print(amazon_phones)
# slicing
print(amazon_phones[2:6:2])
# every other one 
# ['Nokia', 'Sony', 'HTC', 'Panasonic']
print(amazon_phones[0::2])

# lists are mutable 
# replacing 
amazon_phones[0] = 'Apple'
print(amazon_phones)
