#multiple inheritance


class User(object):
    def __init__ (self, name, power):
        self.name = name
        self.power = power
        print('init complete')
        
    def attack(self):
        print(f'attacking {self.power} power')

class Wizard(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'')
        
wizard1 = Wizard('Elf', 100)
# print(wizard1.email)