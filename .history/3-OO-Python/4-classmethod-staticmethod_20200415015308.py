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
    #cls = class
    def adding_things(cls, num1, num2):
        return num1 + num2
    
    @classmethod
    #cls = class
    def adding_things1(cls, num1, num2):
        return cls( 'Teddy', num1 + num2)
    
    @staticmethod
     #cls = class
    
    
    
    
    
player1 = PlayerCharacter('Josh', 23)
print(player1.adding_things(2,3))

#@classmethod does not require instatiating a class
print (PlayerCharacter.adding_things(12,3))

player3 = PlayerCharacter.adding_things ( 900, 90)
print(player3)