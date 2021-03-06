# OOP

class PlayerCharacter :
    # class object attribute - it is static
    membership = True
    # constructor method / init method
    def __init__(self, name, age):
            self.name = name #attributes
            self.age = age
        
    def run (self, hello):
        print('running')
        return 'Workout is done'
    
    def shout(self):
        print(f'My name is {self.name}!')


player1 = PlayerCharacter('Josh', 23)
player2 = PlayerCharacter('Tony', 10)


#blueprint of the object
# help(player1)
# help(list)

#attributes - dynamic data - F.E,  name, age

print(player1.shout())
print(player2.shout())
