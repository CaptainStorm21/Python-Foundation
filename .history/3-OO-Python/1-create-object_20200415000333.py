# OOP

class PlayerCharacter :
    # constructor method / init method
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run (self):
        print('running')
        
player1 = PlayerCharacter('Josh', 23)
player2 = PlayerCharacter('Morgan', 22)

print(player1.age, player1.name)
print(player2.name, player2.age)