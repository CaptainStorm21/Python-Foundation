#inheritance

class User:
    def sign_in(self):
        print('logged in')
    
class Wizard(User):
    pass
    
class Archer(User):
    pass

wizards