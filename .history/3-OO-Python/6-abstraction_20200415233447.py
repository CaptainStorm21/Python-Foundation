class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run (self):
        print('run')
        
    def speak(self):
        print(f'my name is {self.name}. I am {self.age}')
        
player1 = PlayerCharacter('Andy', 1000)
# player1.speak()
# print((1,2,3,1).count(1))
# print(len((1,2,3,1)))
player1.speak = 'speak with me'
print(player1.speak)