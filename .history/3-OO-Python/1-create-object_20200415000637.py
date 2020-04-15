# OOP

class PlayerCharacter :
    # constructor method / init method
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age
        
    def run (self):
        print('running')
        return 'Workout is done'
        
player1 = PlayerCharacter('Josh', 23)
player2 = PlayerCharacter('Morgan', 22)
player2.attack=()

print(player1.age, player1.name, player1.run())
print(player2.name, player2.age)
print(player2.attack)