# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    def __init__ (self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        
    
    
# Init user object
steve = User (' Steve Kelvin', 'kelvin@yahoo.com', 34)
print(steve.name)

# Edit property
steve.name = "Steve Williams"
print(steve.name)

janet = User ('Janet Jones', 'janet@yahoo.com', 34)
print(janet.name)
