# return odd numbers

my_list = [20, 32, 13, 24, 83]
def check_for_odd(item):
    return item %2 != 0

print(list(filter(check_for_odd, my_list)))


