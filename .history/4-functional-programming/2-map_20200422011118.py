# map, filter, zip, reduce

# map (action, [1,2,3])

def multiply_2(item):
    return item * 2
print(list(map (multiply_2, [1,2,3])))
#output 2,4,6

print('method 2 ')
my_list = [10, 20, 30]
def multiply_3(item):
    return item * 3
print('modified')
print(list(map (multiply_3, my_list)))
#output 2,4,6
print(my_list)

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(multiply_by2([1,2,3]))