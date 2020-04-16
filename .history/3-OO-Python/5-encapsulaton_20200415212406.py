class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run (self):
        print('run')
        
    def speak(self):
        print(f'my name is {self.name}. I am {self.age}')
        
player1 = PlayerCharacter('Andy', 1000)

print(player1.name)
print(player2.alignment(obj_or_type))
# player1.speak()