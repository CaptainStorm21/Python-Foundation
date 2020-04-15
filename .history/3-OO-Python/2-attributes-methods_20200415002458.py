# OOP

class PlayerCharacter :
    # class object attribute - it is static
    membership = True
    
    # constructor method / init method
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age
        
    def run (self):
        print('running')
        return 'Workout is done'
        
player1 = PlayerCharacter('Josh', 23)
# player2 = PlayerCharacter('Morgan', 22)
# player2.attack=('Player is attacking !')

#blueprint of the object
# help(player1)
# help(list)

#attributes - dynamic data - F.E,  name, age

print()