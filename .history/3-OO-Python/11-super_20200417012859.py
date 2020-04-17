
class User(object):
    def __init__ (self, email):
        self.email = email
        
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
       self.name = name
       self.power = power
    
    def attack(self):
        #User default attack function show in prompt
        User.attack(self)
        print(f'attacking {self.power} power')
        
class Archer(User):
    def __init__(self, name, arches):
       self.name = name
       self.arches = arches
    
    def attack(self):
        print(f'attacking with {self.arches} arrows')

wizard1 = Wizard('Merlin', 50 )
print(wizard1.email)