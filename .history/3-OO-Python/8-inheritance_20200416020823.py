#inheritance

class User:
    def sign_in(self):
        print('logged in')
    
class Wizard(User):
c
    
class Archer(User):
    pass

wizard1 = Wizard()
print(wizard1.sign_in())
print(wizard1.attack())