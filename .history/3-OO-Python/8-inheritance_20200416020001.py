#inheritance

class User:
    def sign_in(self):
        print('logged in')
    
class Wizard(User):
   def __init__ (self, name, power):
       self.name = name
       self.power = power
    
    def attack():
        print(f'{self.power} has been instatiated')
    
class Archer(User):
    pass

wizard1 = Wizard()
print(wizard1.sign_in())