#
        
    def speak(self):
        print(f'my name is {self.name}. I am {self.age}')
        
player1 = PlayerCharacter('Andy', 1000)
player1.name = 'Wolverine'
player1.speak = 'BooBoo!'

print(player1.speak)