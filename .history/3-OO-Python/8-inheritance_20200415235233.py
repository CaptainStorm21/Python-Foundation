#private put undercore if you need private
# double undercore mean d not overwrite this
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def run (self):
        print('run')
        
    def speak(self):
        print(f'my name is {self._name}. I am {self._age}')
        
player1 = PlayerCharacter('Andy', 1000)

print(player1.speak)