#unformatted strings
name  = 'Johnny Kroft'
age = 22
print ('Good morning ' + name + '! ' + 'You are ' + str(age))

print ('{} turned today {}'.format('Anthony Duma', 23))
print ('{} turned today {}'.format(name, age))
print ('{0} turned today {1}'.format(name, age))

print ('{new_name} flew to {city}'.format(new_name="Michael Cage", city='Paris'))

# formatted strings
print(f'Your name is {name}.  You turned {age +1} today')

