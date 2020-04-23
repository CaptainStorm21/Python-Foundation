#set - only unique
my_list = { char for char in 'Good Boy1'}
print (my_list)


sample_dict = {
    'a': 'Hello'
}

my_dct = { key: value **2 for key, value in  sample_dict}