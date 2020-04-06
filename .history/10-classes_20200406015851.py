# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    def _init_ (self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
# Init user object
steve = User (' Steve Kelvin', 'kelvin@yahoo.com')
