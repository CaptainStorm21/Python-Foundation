#private
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self.age = age
        
    def run (self):
        print('run')
        
    def speak(self):
        print(f'my name is {self.name}. I am {self.age}')
        
player1 = PlayerCharacter('Andy', 1000)
player1.name = 'Wolverine'
player1.speak = 'BooBoo!'

print(player1.speak)