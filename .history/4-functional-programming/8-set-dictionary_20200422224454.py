#set - only unique
my_list = { char for char in 'Good Boy1'}
print (my_list)


sample_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

my_dct = { key: value  for key, value in  sample_dict()}
print(my_dct )