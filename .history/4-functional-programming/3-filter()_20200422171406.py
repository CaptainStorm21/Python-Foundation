# return odd numbers

my_list = [20, 32, 13, 24, 83]
def check_for_odd(item):
    return item %2 != 0

print(list(filter(check_for_odd, my_list)))


list_one = [90, 231,33,11,100]
list_two = [90, 2123, 33, 22, 231,33,11,100]
print(list(zip(list_))