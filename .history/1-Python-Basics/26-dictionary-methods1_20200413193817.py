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

