#list, set, dicitonary

my_list = []

for char in 'HELLO':
    my_list.append(char)
    
print(my_list)



dict_list = [char for char in 'good morning']
print(dict_list)


num_list = [num for num in range (0, 100)]
print(num_list)

print("divide by 3 with no remainder")
num_list3 = [num for num in range (0, 100)  if(num%3 ==0)]
print(num_list3)