# map, filter, zip, reduce

# map (action, [1,2,3])

def multiply_2(item)
print(list(map (multiply_2, [1,2,3])))



# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(multiply_by2([1,2,3]))