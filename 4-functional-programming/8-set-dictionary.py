#set - only unique
my_list = { char for char in 'Good Boy1'}
print (my_list)


sample_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

my_dct = { key: value*2  for key, value in  sample_dict.items()}
print(my_dct )


my_dict_list = { num: num * 2 for num  in [3,2,33,11]}
print (my_dict_list)