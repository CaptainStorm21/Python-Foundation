# list unpacking
# basket = [1,3,5]
# print(basket)


# a,b,c=[1,2,3]
# print(b)
# print(c)

#to unpack
a,b,c, *other=[1,2,3, 21, 33, 322, 52, 34, 23, 4]
print(a)
print(b)
print(c)
print(other)

x, y, z, *numRest, q = [10, 20, 30, 40, 70,90,60]
print(x)
print(y)
print(z)
print(numRest)
print(q)