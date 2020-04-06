# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 8

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values


# simple if
if x == y:
    print(f'{x} is equal to {y}')

#  If/else
if x > y:
    print(f'{x} is greater than {y}')
else:
        print(f'{x} is less than {y}')
        
#  If/elif/else
if x > y:
    print(f'{x} is greater than {y}')
if x == y:
    print(f'{x} is equal to {y}')
else:
        print(f'{x} is less than {y}')
        
# nested If
if x > 2:
    if x<=10:
        print(f'{x} is greater than {y} and x is greater than 2')
        
# Logical operators (and, or, not) - Used to combine conditional statements
if x > 2 and x <= 10:
            print(f'{x} is greater than {y} and x is greater than 2')

#not
if not (x == y ):
    print(f'{x} does not equal to {y}')



# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [90, 2, 1, 4, 5, 6, 20, 10]

if x in numbers: 
    print(x in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
