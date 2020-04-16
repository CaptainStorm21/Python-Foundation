#inheritance

class User:
    def sign_in(self):
        print('logged in')
    
class Wizard(User):
   def __init__ (self, name, power):
       self.name = name
       self.power = power
    
    def attack():
        print(f 'attacking with {self.power}' )
    
class Archer(User):
   def __init__ (self, name, num_arrows):
       self.name = name
       self.num_arrows = power
    
    def attack():
        print(f 'attacking with {self.power}' )
    

wizard1 = Wizard()
print(wizard1.sign_in())
print(wizard1.attack())