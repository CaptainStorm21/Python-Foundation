# purpose 
# clear and understandable
# easy to extend
# easy to maintain
# memory efficient
# DRY (dont repeat yourself)

# functional programming paradagm = pure functions
#another side effect     new_list = [] 

def multiply_by2(li):
    #does not touch anything outside of function
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

#produces the same code
print(multiply_by2([1,2,3]))

#if we convert 
#from 
#         return new_list  to     return print (new_list)
# from
# print(multiply_by2([1,2,3])) to multiply_by2([1,2,3])
# we wil have side effect because it interacts with outer world