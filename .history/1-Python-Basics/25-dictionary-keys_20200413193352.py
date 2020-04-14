# Dictionary key has to be immutable 
# do not create an array as a key 

game_archive = {
    'weapons': [1,2,3],
    'greeting': "Good day",
    'is_Magic': True
}

print(game_archive['a'[1]])
