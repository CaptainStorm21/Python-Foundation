def multiply_by2(li):
    #does not touch anything outside of function
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

#produces the same code
print(multiply_by2([1,2,3]))