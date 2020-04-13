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
# replacing Sharp with Apple
amazon_phones[1] = 'Apple'
print(amazon_phones)
print('slicing updating list')
print(amazon_phones[1:3])

sliced_phones = amazon_phones[4:6]
print(amazon_phones)