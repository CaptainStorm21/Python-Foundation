# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Developer'
language = 'Python'
yearsDev= 13

print ('Hello ' + name)
print (language + ' ' + name)
print ('I have been developing for ' + str(yearsDev) + ' years' )

# String Formattingy




# Arguments by positions
print ('{},  {}, {}, {}' .format ('a' , 'b', 'c', 'd'))
print ('{},  {}, {}, {}'.format ('one' , 'two', 'zero', 'three'))

# Argument by Name 
print ('I am an {name} and I have {yearsDev}'.format(name = 'Engineer', yearsDev = '3')+ ' years experience')
print ('I am an {name} and I have {yearsDev}'.format(name = name, yearsDev = yearsDev )+ ' years experience')

#F-string 3.6+
print (f' I am {name} with {yearsDev} years exp ')

# String Methods
s = "welcome to python"
print(s.capitalize())

#All caps
print(s.upper())

#All small 
print(s.lower())

#swap
greeting = "good morning"
print (greeting.swapcase())

#length
print(len(greeting))

#replace
print(greeting.replace('morning', 'night'))

#count
greeting1 = "merry adventures"
sub = "m"
print(greeting1.count(sub))

#find a place
print (greeting1.find('v'))

#numeric
print(greeting.isnumeric())

yearDev = '100'
print(yearDev.isnumeric())

print(yearDev.isalpha())
print(yearDev.isalnum())
print(yearDev.rstrip())