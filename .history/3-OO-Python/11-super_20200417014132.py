
class User(object):
    def __init__ (self, email):
        self.email = email
        
    def sign_in(self):
        print('logged in')

# class Wizard(User):
#     def __init__(self, name, power, email):
#         User.__init__(self, email)
#         self.name = name
#         self.power = power
# 

class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power


    
    def attack(self):
        print(f'attacking {self.power} power')
        
wizard1 = Wizard('Merlin', 50, 'wizard@oz.com' )
print(wizard1.email)
