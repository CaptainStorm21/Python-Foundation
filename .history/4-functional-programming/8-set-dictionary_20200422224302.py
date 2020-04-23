#set - only unique
my_list = { char for char in 'Good Boy1'}
print (my_list)


sample_dict = {
    'a': 'Hello',
    'b': 'Good morning',
    'c': 'Good evening',
    'd':''
}

my_dct = { key: value **2 for key, value in  sample_dict}