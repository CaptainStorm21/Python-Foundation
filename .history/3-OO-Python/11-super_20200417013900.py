
class User(object):
    def __init__ (self, email):
        self.email = email
        
    def sign_in(self):
        print('logged in')

class Wizard(User):
    
    
    def attack(self):
        print(f'attacking {self.power} power')
        
wizard1 = Wizard('Merlin', 50 )
# print(wizard1.email)
# print(wizard1.sign_in())