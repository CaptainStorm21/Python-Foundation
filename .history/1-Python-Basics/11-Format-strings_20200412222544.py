#unformatted strings
name  = 'Johnny Kroft'
age = 22
print ('Good morning ' + name + '! ' + 'You are ' + str(age))

print ('{} turned today {}'.format('Anthony', 23))
print ('{} turned today {}'.format(name, age))
print ('{0} turned today {1}'.format(name, age))

# formatted strings
print(f'Your name is {name}.  You turned {age +1} today')

