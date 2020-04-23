#set - only unique
my_list = { char for char in 'Good Boy1'}
print (my_list)


sample_dict = {
    'a': 1,
    'b': 'Good morning',
    'c': 'Good evening',
    'd':'Good bye'
}

my_dct = { key: value  for key, value in  sample_dict()}
print(my_dct )