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
person2 = person.copy()
print(person2)
person2['city'] = 'Vancuver'
print(person2)

#remove item
del(person2['city'])
person2.pop('age')
print(person2)

# Clear
person2.clear()
print(person2)
print(len(person2))

print(person)
print(person2)

# List of dict
people = [
    {'name': 'Alice Closer', 'age': 10},
    {'name': 'Bob Bryant', 'age': 30}
]
print(people)
print(people[1])