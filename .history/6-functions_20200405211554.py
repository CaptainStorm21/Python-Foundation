# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def sayHello():
    print('Hello World')
    
sayHello()

def sayGoodMorning (name = 'Alfed'):
    print('Good mornig ' + name)

sayGoodMorning('Morgan')
sayGoodMorning()

# Return a value
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(2, 3))

#increment
def addOnetoNum(num):
    num = num + 1
    return num
addOnetoNum

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

