#inheritance

class User():
    def sign_in(self):
        print('logged in')
    
class Wizard(User):
    def attack():
        print(f'  ')
   def __init__ (self, name, power):
       self.name = name
       self.power = power
