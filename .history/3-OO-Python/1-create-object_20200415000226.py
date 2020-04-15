# OOP

class PlayerCharacter :
    # constructor method / init method
    def __init__(self, name, age):
        self.name = name
        
    def run (self):
        print('running')
        
player1 = PlayerCharacter('Josh')
print(player1.name)