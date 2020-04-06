# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# Simple Loop
people = ['John', 'Mary', 'Anna', 'Margaret', 'Sylvia']
for person in people:
    print('Current person is: ', person)
    
# Break
people1 = ['John', 'Mary', 'Anna', 'Margaret', 'Sylvia', 'Monique']
for person in people1:
            # break
    if person == 'Anna':
        break
        print('Current person is: ', person)
    

# While loops execute a set of statements as long as a condition is true.
