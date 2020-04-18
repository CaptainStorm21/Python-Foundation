#multiple inheritance


class User(object):
    def __init__ (self, name, power):
        self.name = name
        self.power = power
        print('init complete')
        
    def attack(self):
        print(f'attacking {self.power} power')

class Wizard(User):
    def __init__(self, name, swords):
        self.name = name
        self.swords = swords

    def check_swords(self):
        print(f'spare {self.swords}  remaining')
    
    def shield (self):
        print('i am shielding')
        
class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows}  remaining')
    
    def run (self):
        print('i am running')
        
class HybridBorg(Wizard, Archer):
    pass

hb1 = HybridBorg('Elven', 100)
print(hb1.run())