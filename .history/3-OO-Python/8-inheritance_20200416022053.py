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
        
class Archer(User):
    def __init__(self, name, arches):
       self.name = name
       self.arches = arches
    
    def attack():
        print(f'attacking with {self.archer}')

wizard1 = Wizard