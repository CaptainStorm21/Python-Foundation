# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    def __init__ (self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    def has_birthday(self):
        self.age +=1
    
class Customer (User):
    def __init__ (self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

def set_balance(self, balance):
        self.balance = balance

def greeting(self):
     return f'My name is {self.name} and I am {self.age} and I owe {self.balance}'

# Init user object
steve = User (' Steve Kelvin', 'kelvin@yahoo.com', 34)
print(steve.name)

# Edit property
steve.name = "Steve Williams"
print(steve.name)

janet = User ('Janet Jones', 'janet@yahoo.com', 34)
print(janet.name)


print("Janet's birthday is ", janet.has_birthday())
print(janet.greeting())

# Init customer
john = Customer ("John Meyer", 'john@yahoo.com', 32)
john.set_balance(324)
print(john.name)
print(john.greeting())

