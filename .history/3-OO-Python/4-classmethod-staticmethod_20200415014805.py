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

    @classmethod
    def adding_things(num1, num2):
        return num1 + num2
    

player1 = PlayerCharacter('Josh', 23)
print()
