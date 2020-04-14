# Short Circuting

is_Friend = True
is_User = True

if is_Friend or is_User:
    print("both are true")

if is_Friend and is_User:
    print("both are true")
    
age = 15
year = 2019
boy = "Vlad"

if age < 20:
    print(f'{age} of the boy is less than 20')

if year > 1900