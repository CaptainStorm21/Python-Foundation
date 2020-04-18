#multiple inheritance


class User(object):
    def __init__ (self, name, power):
        self.name = email
        print('init complete')
        
    def sign_in(self):
        print('logged in')
        

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking {self.power} power')
        
wizard1 = Wizard('Merlin', 50, 'wizard@oz.com' )
# print(wizard1.email)