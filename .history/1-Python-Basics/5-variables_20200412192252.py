# variable is a way to store the information
# General rules of naming a variable

# start with lower case or underscore
# letter, number underscore
# case sensitive


age = 90
print(age)

# snake_case  / camel_case
user_age= 20
print(user_age)

# private variable
_user_income = 9000
print(_user_income)

#not valid variable
# 2cows = "2 cows"
# print(2cows)

# don't overwrite keywords
# print = 'printing screen'
# print(print)

#reassigneable
user_birth_year = 2000
city_age_difference = user_birth_year - 1880
print ( city_age_difference)
age_difference = 2020 - city_age_difference
print ( age_difference )

#constant
#values will never change
PI = 3.14

#do not create a variable with double underscore
# __greeting = "hello "

a, b, c = 1, 2, 3
print(a)
