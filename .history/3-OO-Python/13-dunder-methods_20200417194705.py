# you can overwrite built in dunder __whatever__()

class Toy():
    def __init__ (self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __call__ (self):
        return('yes!')

action_figure  = Toy ('red', 10)
print(action_figure.__str__())
# print(str(action_figure))
print(str(action_figure))
print(len(action_figure))
print(action_figure())