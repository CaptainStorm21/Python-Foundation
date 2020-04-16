class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # def run (self):
    #     print('run')
        
    # def speak(self):
    #     print(f'my name is {self.name}. I am {self.age}')
        
player1 = PlayerCharacter('Andy', 1000)
print(player1.name)
print(player1.age)
# player1.speak()

player3 = { 'name': 'andrei', 'age': 100}
print(player3['name'])
print(player3['age'])
