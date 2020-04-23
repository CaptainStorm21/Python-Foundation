#zip grabs 1 of each and zip them 
list_one = [90, 231,33,11,100]
list_two = [12, 2123, 33, 22, 231,33,11,100]
print(list(zip(list_one, list_two)))
print(list_one)

#output 
# [(90, 12), (231, 2123), (33, 33), (11, 22), (100, 231)]
# [90, 231, 33, 11, 100]

#tuple will work here as well (232, 22, 11, 534)