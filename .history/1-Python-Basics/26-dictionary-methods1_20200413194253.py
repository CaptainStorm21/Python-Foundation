# Dictionary methods

game_archive = {
    'weapons': [1,2,3],
    'greeting': "Good day",
    'is_Magic': True
}

print(game_archive['weapons'])

# print(game_archive['age]) - does not exist - error
# workaround
print(game_archive.get('age'))
#output None

#if you want a default value 
print(game_archive.get('age', 'ancient'))

user = dict(name= 'Brave Elf')
print(user)

# does weapons exist in game_archive
print ( 'weapons'  in user)

