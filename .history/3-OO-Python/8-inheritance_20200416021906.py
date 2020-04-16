# inheritance


class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
       self.name = name
       self.power = power
    
    def attack():
        print(f'attacking {self.power}')
        
class Wizard(User):
    def __init__(self, name, power):
       self.name = name
       self.power = power
    
    def attack():
        print(f'attacking {self.power}')