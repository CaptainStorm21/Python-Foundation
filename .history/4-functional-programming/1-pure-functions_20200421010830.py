# purpose 
# clear and understandable
# easy to extend
# easy to maintain
# memory efficient
# DRY (dont repeat yourself)

# functional programming paradagm = pure functions

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

multiply_by2([])