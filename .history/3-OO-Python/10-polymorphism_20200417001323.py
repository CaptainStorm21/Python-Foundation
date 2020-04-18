#  polymorphism - share  methods by classes

class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
       self.name = name
       self.power = power
    
    def attack(self):
        print(f'attacking {self.power} power')
        
class Archer(User):
    def __init__(self, name, arches):
       self.name = name
       self.arches = arches
    
    def attack(self):
        print(f'attacking with {self.arches} arrows')

wizard1 = Wizard('Merlin', 50 )
archer1 = Archer('Elven', 150 )

# def player_attack(char):
#     char.attack()
    
# player_attack(wizard1)
# player_attack(archer1)

for char in [wizard1, archer1]