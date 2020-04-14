# Dictionary
# unordered value / key pair
# each value/key pair is located in different memory locations

my_list = [
    {
        'a': [3, 2, 34, 123],
        'b': 'Vikings were roaming around...',
        'c': True
    },
    {
        'a': ['Bob Marley', 'Jon Bon Jovi', 'Aerosmith'],
        'b': 'USA',
        'c': True
    }
]

print(my_list[0]['a'][2])

