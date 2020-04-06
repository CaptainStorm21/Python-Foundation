# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# simple effect
person = {
    'first_name': 'Jonathan',
    'last_name': 'Jones',
    'age' :  90
}

print(person)

# Using a constructor
client1 = dict ( first_name = 'Alex', last_name = 'Naval', age = 20 )
print(client1)
print(client1['first_name'])
print(client1.get('first_name'))

#add key /value
client1['phone'] = '333-234-3424'
print(client1)

#print only keys
print(person.keys())

#print only values
print(person.items())


#make a copy
